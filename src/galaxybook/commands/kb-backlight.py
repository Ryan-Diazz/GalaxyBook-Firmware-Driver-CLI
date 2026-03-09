from galaxybook.utils import read, write

FILE_PATH = "/sys/class/leds/samsung-galaxybook::kbd_backlight/brightness"
FILE_PATH_MAX = "/sys/class/leds/samsung-galaxybook::kbd_backlight/max_brightness"


# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser(
        "kb-light",
        help="Manage keyboard backlight"
    )

    actions = parser.add_subparsers(dest="action")

    # show
    show_parser = actions.add_parser(
        "show",
        help="Show keyboard backlight level"
    )
    show_parser.set_defaults(
        func=handle_show,
        requires_root=False
    )

    # set
    set_parser = actions.add_parser(
        "set",
        help="Set keyboard backlight brightness"
    )

    set_parser.add_argument(
        "value",
        type=int,
        help="Brightness percentage (0-100)"
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
    current = current_level()
    maximum = maximum_level()

    percent = ((current) / (maximum)) * 100 if maximum else 0

    print("Keyboard Backlight".center(40, "-"))
    print(f"{'Level:':20} {percent:.1f}%")
    print("-" * 40)


def set_value(value):
    if value is None:
        print("Please specify a brightness value (0-100).")
        return

    elif not 0 <= value <= 100:
        print("Brightness must be between 0 and 100.")
        return

    else:
        maximum = maximum_level()
        new_value = round((value / 100) * maximum)
        new_value = max(0, min(maximum, new_value))

        write(FILE_PATH, new_value)

        percent = ((new_value) / (maximum)) * 100 if maximum else 0
        print(f"Keyboard backlight set to {percent:.1f}%.")


def current_level():
    value = int(read(FILE_PATH))
    return value

def maximum_level():
    value = int(read(FILE_PATH_MAX))
    return value
