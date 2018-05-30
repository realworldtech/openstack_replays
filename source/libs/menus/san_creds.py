import npyscreen, os, signal
class AskForCredentials(npyscreen.Form):
    def create(self):
        self.name = "Storage Manager Credentials"
        title_blurb = "Please enter the Storage Manager Admin credentials."
        self.add(npyscreen.FixedText, value=title_blurb)
        self.add(npyscreen.FixedText, value="It is very important that this user has full administrative access to the SMC")

        self.address    = self.add(npyscreen.TitleText, name="SMC IP:", value='172.21.0.60')
        self.port       = self.add(npyscreen.TitleText, name="Port:", value='3033')
        self.username   = self.add(npyscreen.TitleText, name="Username:", value='admin')
        self.password   = self.add(npyscreen.TitlePassword, name="Password:")

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.edit()
        return (
                form.address.value,
                form.port.value,
                form.username.value,
                form.password.value,
            )
    @classmethod
    def run(self):
        return npyscreen.wrapper_basic(self.wrapme)
