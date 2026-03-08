import subprocess
from galaxybook.utils import perm, read, write

FILE_PATH = "/sys/class/firmware-attributes/samsung-galaxybook/attributes/block_recording/current_value"

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser("recording", help="Manage the 'Recording Block' from the samsung-galaxybook firmware")

    actions = parser.add_subparsers(dest="action")

    #show
    show_parser = actions.add_parser("show", help="shows current Recording Block status")
    show_parser.set_defaults(
        func=handle_show,
        requires_root=False
    )

    #toggle
    toggle_parser = actions.add_parser("toggle", help="toggles current Recording Block status between on and off")
    toggle_parser.set_defaults(
        func=handle_toggle,
        requires_root=True
    )


    #on
    on_parser = actions.add_parser("on", help="turns Recording Block status off (enabling recording)")
    on_parser.set_defaults(
        func=handle_on,
        requires_root=True
    )

    #on
    off_parser = actions.add_parser("off", help="turns Recording Block status on (disabling recording)")
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
        print("Recording Block: ON (Camera Deactivated)")
    else:
        print("Recording Block: OFF (Camera Activated)")


def already(value):
    if str(value) == "1":
        print("Recording Block: Already ON (Camera Deactivated)")
    else:
        print("Recording Block: Already OFF (Camera Activated)") 


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