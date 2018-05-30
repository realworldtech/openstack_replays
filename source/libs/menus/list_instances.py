import npyscreen, os, signal
from functools import partial
class ListInstances(npyscreen.Form):
    def create(self):
        self.name = "Openstack Instances"
        title_blurb = "Please select which instance(s) you wish to restore:"
        self.select_menu = self.add(npyscreen.TitleMultiSelect, name="Instances:")

    def set_instances(self, instances):
        list_of_instances = [instance.name for instance in instances]
        self.select_menu.values = list_of_instances

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.set_instances(args[0])
        form.edit()
        return form.select_menu.value
    @classmethod
    def run(self, instances):
        return npyscreen.wrapper_basic(partial(self.wrapme, instances))
