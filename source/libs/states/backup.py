from libs.menus import os_creds, list_projects

##
# OpenStack Libraries
##
from openstack import connection, profile
import npyscreen

class BackupState:
    @classmethod
    def run(self, log):
        log.debug("Inside the backup state classmethod")
        inst = BackupState(log)
        # Get creds of main install
        inst.get_creds() \
                .make_connection() \
                .backup_projects()
    ###
    # Instance Methods here on
    ###
    def __init__(self, log):
        self._log = log
        self._log.debug("Initialised BackupState")

    def get_creds(self):
        (
            self._url,
            self._username,
            self._password,
            self._domain,
            self._project
        ) = os_creds.AskForCredentials.run()
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


    def backup_projects(self):
        self._log.info("Initialising backup of projects")
        projects = list(self._conn.identity.projects())
        self._log.debug("Asking user for projects")
        selections = list_projects.ListProjects.run(projects)
