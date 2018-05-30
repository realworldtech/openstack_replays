import npyscreen, os, signal
class AskForCredentials(npyscreen.Form):
    def create(self):
        self.name = "Openstack Credentials"
        title_blurb = "Please enter the OpenStack Credentials to login as Admin."
        self.add(npyscreen.FixedText, value=title_blurb)
        self.add(npyscreen.FixedText, value="It is very important that this user has full administrative access to the openstack instance")

        #self.add(npyscreen.TextFild, value="OS URL:")
        self.url = self.add(npyscreen.TitleText, name="OpenStack URL:", value='https://<openstack.url>:5000/v3')
        self.domain   = self.add(npyscreen.TitleText, name="Domain:", value='Default')
        self.project  = self.add(npyscreen.TitleText, name="Default Project:", value='admin')
        self.username = self.add(npyscreen.TitleText, name="OS Username:", value='admin')
        self.password = self.add(npyscreen.TitlePassword, name="OS Password:")

    @classmethod
    def wrapme(self, *args):
        form = self()
        form.edit()
        return (
                form.url.value,
                form.username.value,
                form.password.value,
                form.domain.value,
                form.project.value
            )
    @classmethod
    def run(self):
        return npyscreen.wrapper_basic(self.wrapme)
