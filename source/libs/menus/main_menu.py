#
# Main Menu - Entry point
#
from cursesmenu.items import *
from cursesmenu import SelectionMenu, CursesMenu


class MainMenu:
    @classmethod
    def run(self):
        menu = CursesMenu("Openstack Toolset", "Restore OpenStack Virtual Machine Block Device from SAN - By Real World")
        options = ['Restore State']

        for idx, item in enumerate(options):
            menu.append_item(SelectionItem(item, idx))

        submenu = CursesMenu("Contact the Author.")
        contact = SubmenuItem("Author: Karl Kloppenborg", submenu=submenu)
        contact2 = SubmenuItem("Email: kkloppenborg@rwts.com.au", submenu=submenu)
        submenu.append_item(contact)
        submenu.append_item(contact2)

        sub = SubmenuItem("Help!", submenu, menu=menu)
        menu.append_item(sub)

        menu.show()
        return menu.selected_option
