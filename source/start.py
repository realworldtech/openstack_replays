#
# OpenMover - Runtime for backup, restore and transitioning OpenStack.
#
import signal, os
from libs.menus.main_menu import MainMenu
from libs.log import Logging

from libs.states.backup import BackupState
###
# Selection Options
###

def backup_state(log):
    log.info("Starting backup state option")
    BackupState.run(log)

def restore_state(log):
    log.info("Starting restore state option")
def migrate_state(log):
    log.info("Starting migrate state option")
def quit(log):
    log.info("Exiting program")
    exit(0)

def signal_handler(signal, frame):
    os.system('clear')
    print('You pressed Ctrl+C! - Leaving')
    exit(0)
###
# Main Exection
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    # Lets start the main menu.
    l = Logging("OpenMover")
    l.info("Logger started")
    l.debug("Opening menu")
    selection = MainMenu.run()
    l.debug("Menu Selection was: %d" % selection)

    select_options = [
            'backup_state',
            'restore_state',
            'migrate_state']

    if selection is 4:
        quit(l)

    # Hit up the local list of defined methods
    locals()[select_options[selection]](l)


