import subprocess
from galaxybook.utils import perm

FILE_PATH = "/sys/class/firmware-attributes/samsung-galaxybook/attributes/power_on_lid_open/current_value"

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser("powerlid", help="Manage power on lid open firmware attribute")

    actions = parser.add_subparsers(dest="action")

    #show
    show_parser = actions.add_parser("show", help="shows current 'power on lid open status'")
    show_parser.set_defaults(
        func=handle_show,
        requires_root=False
    )

    #toggle
    toggle_parser = actions.add_parser("toggle", help="toggles current 'power on lid open status' between on and off")
    toggle_parser.set_defaults(
        func=handle_toggle,
        requires_root=True
    )


    #on
    on_parser = actions.add_parser("on", help="turns 'power on lid open' off (enabling recording)")
    on_parser.set_defaults(
        func=handle_on,
        requires_root=True
    )

    #on
    off_parser = actions.add_parser("off", help="turns 'power on lid open' on (disabling recording)")
    off_parser.set_defaults(
        func=handle_off,
        requires_root=True
    )

    parser.set_defaults(func=lambda args: parser.print_help())


# ------------------
# handlers
# ------------------
def handle_show(args):
    show()

def handle_toggle(args):
    toggle()

def handle_on(args):
    set_value(0)

def handle_off(args):
    set_value(1)


# ------------------
# command implementations
# ------------------
def show():
    current = read(FILE_PATH)
    if current == "1":
        print("Power On Lid Open: Activated")
    else:
        print("Power On Lid Open: Deactivated")


def already(value):
    if str(value) == "1":
        print("Power On Lid Open: Already Activated")
    else:
        print("Power On Lid Open: Already Deactivated")
    

def set_value(value):
    if read(FILE_PATH) == str(value):
        already(value)
    else:
        write(FILE_PATH, value)
        show()


def toggle():
    if read(FILE_PATH) == "0":
        set_value(1)
    else:
        set_value(0)