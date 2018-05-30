import npyscreen, os, signal
from functools import partial
class ListReplays(npyscreen.Form):
    def create(self):
        self.name = "Replay Selection"
        title_blurb = "Please select which Replay(snapshot) you wish to restore:"
        self.select_menu = self.add(npyscreen.TitleSelectOne, name="Replays:")

    def set_data(self, volume, data):

        list_of_data = ['%s - %s' % (volume.selection_name, selection['instanceName']) for selection in data]
        self.select_menu.values = list_of_data

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.set_data(args[0], args[1])
        form.edit()
        return form.select_menu.value
    @classmethod
    def run(self, volume, data):
        return npyscreen.wrapper_basic(partial(self.wrapme, volume, data))
