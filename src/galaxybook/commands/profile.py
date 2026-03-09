from galaxybook.utils import read, write, perm

FILE_PATH_PROFILE = "/sys/firmware/acpi/platform_profile"
FILE_PATH_CHOICES = "/sys/firmware/acpi/platform_profile_choices"

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser("profile", help="Manage performance mode profile")

    actions = parser.add_subparsers(dest="action")

    # show command
    show_parser = actions.add_parser("show", help="Show current performance mode profile")
    show_parser.set_defaults(
        func=handle_show,
        requires_root=False
    )

    # set command
    set_parser = actions.add_parser("set", help="Set performance mode profile")
    set_parser.add_argument(
        "name",
        type=str,
        help="Profile name (see available choices with show)"
    ).completer = profile_completer
    set_parser.set_defaults(
        func=handle_set,
        requires_root=True
    )

    parser.set_defaults(func=lambda args: parser.print_help())

# ------------------
# handlers
# ------------------
def handle_show(args):
    show("Performance Profile")

def handle_set(args):
    set_value(args.name)


# ------------------
# command implementations
# ------------------
def show(title):
    current = current_profile()
    choices = choices_profile()

    print(f"{title}".center(40, "-"))

    for profile in choices:
        marker = "*" if profile == current else " "
        print(f"{marker} {profile}")

    print("-" * 40)

def already(value):
    print(f"Performance Profile already set to: {value}")
    print()
    show("Performance Options")

def set_value(name):
    if not name:
        print("Please specify a profile with -n or --name")
        return
    
    choices = choices_profile()
    current = current_profile()

    if name not in choices:
        print("Invalid profile.")
        print(f"Available profiles: {', '.join(choices)}")
        return
    
    elif current == name:
        already(name)

    else:
        write(FILE_PATH_PROFILE, name)
        show(f"Performance profile set")
    


def current_profile():
    value = read(FILE_PATH_PROFILE).strip()
    return value

def choices_profile():
    value = read(FILE_PATH_CHOICES).strip()
    choices = value.split()
    return choices

def profile_completer(prefix, **kwargs):
    return choices_profile()
