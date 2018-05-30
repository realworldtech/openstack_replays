from libs.menus import os_creds, san_creds, list_instances, list_volumes, list_replays
from libs.dell_api import StorageCenterApi

##
# OpenStack Libraries
##
from openstack import connection, profile
import npyscreen, os

class RestoreState:

    _ALL_PROJECTS = False

    @classmethod
    def run(cls, log):
        log.debug("Inside the Restore state classmethod")
        inst = cls(log)
        # Get creds of main install
        inst.get_creds() \
                .make_connection()  \
                .select_instances() \
                .select_volumes()   \
                .restore_on_smc()
    ###
    # Instance Methods here on
    ###
    def __init__(self, log):
        self._log = log
        self._log.debug("Initialised %s" % self.__class__.__name__ )

    def get_creds(self):
        (
            self._url,
            self._username,
            self._password,
            self._domain,
            self._project
        ) = os_creds.AskForCredentials.run()

        (
                self.smc_address,
                self.smc_port,
                self.smc_username,
                self.smc_password
        ) = san_creds.AskForCredentials.run()
        return self

    def make_connection(self):
        self._log.debug("About to init connection")
        auth_args = {
            'auth_url': self._url,
            'project_name': self._project,
            'user_domain_name': self._domain,
            'project_domain_name': self._domain,
            'username': self._username,
            'password': self._password,
        }
        self._conn = connection.Connection(**auth_args)
        self._log.info("Connection to %s established!" % self._url)
        return self


    def select_instances(self):
        self._log.info("Getting list of Instances from Openstack.")
        self.instances = list(self._conn.list_servers(detailed=False, all_projects=self._ALL_PROJECTS))
        self._log.debug("Making selection available for restores")
        self.instance_selections = list_instances.ListInstances.run(self.instances)
        return self


    def select_volumes(self):
        '''
        Takes the list of selections and then queries the volumes from those servers
        '''
        self.volumes = []
        for instance in self.instance_selections:
            self._log.debug("selection: {}".format(self.instances[instance].name))
            for vd in self.instances[instance].volumes:
                volume_munch = self._conn.get_volume_by_id(vd.id)
                attach_strs = []
                for attachment in volume_munch.attachments:
                    attach_strs.append("Attached: {}".format(attachment.device))
                attach_string = '/'.join(attach_strs)
                volume_munch['selection_name'] = "{server_name} - {attachs}".format(
                        server_name = self.instances[instance].name,
                        attachs = attach_string
                )
                self.volumes.append(volume_munch)

        ###
        # Show the selection of volumes
        ###
        self.volume_selections = list_volumes.ListVolumes.run(self.volumes)
        return self

    def restore_on_smc(self):
        '''
        This is a complicated set of actions,
        for each volume we will ask them which snapshot and restore individually
        '''
        ###
        # Login to SMC
        ###
        smc_api = StorageCenterApi(
                self.smc_address,
                int(self.smc_port),
                self.smc_username,
                self.smc_password,
                False
        )
        smc_api.open_connection()
        self._log.debug("Connection to SMC established")
        for volume_selection_id in self.volume_selections:
            self._log.info("Starting restore process for volume: %s" %
                    self.volumes[volume_selection_id].selection_name)
            ###
            vol = self.volumes[volume_selection_id]
            smc_volume = smc_api.find_volume(vol.id)
            if not smc_volume: self._log.error(
                    "WARNING: VOLUME WITH ID: %s COULD NOT BE FOUND ON SMC" % vol.id
            )
            self._log.info("Getting list of Replays available for volume: %s" % smc_volume['instanceId'])
            smc_replays = smc_api.list_replays(smc_volume)
            if len(smc_replays) < 1: self._log.info("There was no SMC replays available for: %s" %
                    self.volumes[volume_selection_id].selection_name)

            ###
            # Use this as a list and lets make a selection page.
            ###
            replay_selection = list_replays.ListReplays.run(
                    self.volumes[volume_selection_id],
                    smc_replays
                )[0]
            restore_replay = smc_replays[replay_selection]
            self._log.debug("Selected %d" % replay_selection)
            self._log.debug("Going to restore volume from selection: {}".format(
                restore_replay['instanceName']
            ))

            ###
            # New Volume creation
            ###
            new_volume_name = "{volume_name}_snap_{replay_date}".format(
                    volume_name = smc_volume['instanceName'],
                    replay_date = restore_replay['freezeTime'] \
                            .replace(' ', '-') \
                            .replace(':', '_') \
                            .replace('/', '_') \
                            .replace('+','-tz-')
                            )[:52]
            self._log.info("Restoring from Replay: %s to new volume: %s" % (
                restore_replay['instanceName'],
                new_volume_name
            ))

            ###
            # Create the view on the san
            ###
            results = smc_api.create_view(
                    new_volume_name,
                    restore_replay,
                    smc_volume['volumeFolder'],
                    'Created by Openstack Snapshot Tools by Real World Technologies'
            )
            if results:
                self._log.info("Successfully created volume %s" % new_volume_name)



