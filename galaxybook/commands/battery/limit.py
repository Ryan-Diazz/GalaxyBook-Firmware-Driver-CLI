from galaxybook.utils import read, write, perm

FILE_PATH = "/sys/class/power_supply/BAT1/charge_control_end_threshold"

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser("limit", help="Manage battery charge limit from 80%% to 100%%")

    actions = parser.add_subparsers(dest="action")

    # show command
    show_parser = actions.add_parser("show", help="Show current battery limit")
    show_parser.set_defaults(
        func=handle_show,
        requires_root=False
    )

    # set command
    set_parser = actions.add_parser("set", help="Set battery charge limit")
    set_parser.add_argument(
        "value",
        type=int,
        help="Battery charge limit (80–100)"
    )
    set_parser.set_defaults(
        func=handle_set,
        requires_root=True
    )

    parser.set_defaults(func=lambda args: parser.print_help())

# ------------------
# handlers
# ------------------
def handle_show(args):
    show()

def handle_set(args):
    set_value(args.value)


# ------------------
# command implementations
# ------------------
def show():
    value = read(FILE_PATH)
    print(f"Current charge threshold: {value}%")

def already(value):
    print(f"Batter limit already set to {value}%")

def set_value(value):
    if not 80 <= value <= 100:
        print("Battery limit must be between 80% and 100%.")
        return
    
    current = int(read(FILE_PATH))

    if current == value:
        already(value)

    else:
        write(FILE_PATH, value)
        print(f"Battery limit set to {value}%")