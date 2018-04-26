import npyscreen, os, signal
from functools import partial
class ListProjects(npyscreen.Form):
    def create(self):
        self.name = "Openstack Projects"
        title_blurb = "Please select which projects you wish to backup:"
        self.projects = self.add(npyscreen.TitleMultiSelect, name="Projects:")

    def set_projects(self, projects):
        list_of_projects = [proj.name for proj in projects]
        self.projects.values = list_of_projects

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.set_projects(args[0])
        form.edit()
        return form.projects.value
    @classmethod
    def run(self, projects):
        return npyscreen.wrapper_basic(partial(self.wrapme, projects))
