from galaxybook.utils import read, write, perm

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser(
        "status", 
        help="Show battery status"
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
    status = curr_status()

    capacity = curr_capacity()
    capacity_level = curr_capacity_level()

    voltage = voltage_now() / 1_000_000
    current = current_now() / 1_000_000
    wattage = voltage * current
    
    print("Battery Status".center(40, "-"))
    print(f"{'Status:':20} {status}")
    print(f"{'Charge:':20} {capacity}% ({capacity_level})")
    print(f"{'Power Usage:':20} {wattage:.2f} W")
    print(f"{'Voltage:':20} {voltage:.2f} V")
    print("-" * 40)

def voltage_now():
    FILE_PATH = "/sys/class/power_supply/BAT1/voltage_now"
    value = read(FILE_PATH)
    return float(value)

def current_now():
    FILE_PATH = "/sys/class/power_supply/BAT1/current_now"
    value = read(FILE_PATH)
    return float(value)

def curr_capacity():
    FILE_PATH = "/sys/class/power_supply/BAT1/capacity"
    value = read(FILE_PATH)
    return int(value)

def curr_capacity_level():
    FILE_PATH = "/sys/class/power_supply/BAT1/capacity_level"
    value = read(FILE_PATH)
    return value

def curr_status():
    FILE_PATH = "/sys/class/power_supply/BAT1/status"
    value = read(FILE_PATH)
    return value