from galaxybook.utils import read, write, perm

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser(
        "health", 
        help="Show battery health"
    )

    parser.set_defaults(func=handle)

# ------------------
# handlers
# ------------------
def handle(args):
    show()

# ------------------
# command implementations
# ------------------
def show():
    design = charge_design() / 1000
    full = charge_full() / 1000
    now = charge_now() / 1000
    cycles = cycle_count()

    # Health percentage
    health_percent = (full / design) * 100

    # Current charge percentage
    charge_percent = (now / full) * 100 if full else 0

    print("Battery Info".center(40, "-"))
    print(f"{'Design Capacity:':20} {design} mAh")
    print(f"{'Full Charge:':20} {full} mAh")
    print(f"{'Current Charge:':20} {now} mAh ({charge_percent:.1f}%)")
    print(f"{'Health:':20} {health_percent:.1f}%")
    print(f"{'Cycle Count:':20} {cycles}")
    print("-" * 40)

def charge_design():
    FILE_PATH = "/sys/class/power_supply/BAT1/charge_full_design"
    value = read(FILE_PATH)
    return int(value)

def charge_full():
    FILE_PATH = "/sys/class/power_supply/BAT1/charge_full"
    value = read(FILE_PATH)
    return int(value)

def charge_now():
    FILE_PATH = "/sys/class/power_supply/BAT1/charge_now"
    value = read(FILE_PATH)
    return int(value)

def cycle_count():
    FILE_PATH = "/sys/class/power_supply/BAT1/cycle_count"
    value = read(FILE_PATH)
    return int(value)