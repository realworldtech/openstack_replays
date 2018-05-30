import npyscreen, os, signal
from functools import partial
class ListVolumes(npyscreen.Form):
    def create(self):
        self.name = "Volume Selection"
        title_blurb = "Please select which volumes(s) you wish to restore:"
        self.select_menu = self.add(npyscreen.TitleMultiSelect, name="Volumes:")

    def set_data(self, data):
        list_of_data = [selection.selection_name for selection in data]
        self.select_menu.values = list_of_data

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.set_data(args[0])
        form.edit()
        return form.select_menu.value
    @classmethod
    def run(self, data):
        return npyscreen.wrapper_basic(partial(self.wrapme, data))
