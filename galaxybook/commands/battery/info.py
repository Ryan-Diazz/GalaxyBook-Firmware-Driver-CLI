from galaxybook.utils import read, write, perm

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser(
        "info", 
        help="Show battery information"
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
    print(f"Battery Information ({name()})".center(40, "-"))
    print(f"{'Manufacturer:':20} {manufacturer()}")
    print(f"{'Model Name:':20} {model_name()}")
    print(f"{'Serial Number:':20} {serial()}")
    print(f"{'Technology:':20} {technology()}")
    print(f"{'Type':20} {gettype()}")
    print("-" * 40)

def manufacturer():
    FILE_PATH = "/sys/class/power_supply/BAT1/manufacturer"
    value = read(FILE_PATH)
    return value

def model_name():
    FILE_PATH = "/sys/class/power_supply/BAT1/model_name"
    value = read(FILE_PATH)
    return value

def name():
    FILE_PATH = "/sys/class/power_supply/BAT1/hwmon2/name"
    value = read(FILE_PATH)
    return value

def serial():
    FILE_PATH = "/sys/class/power_supply/BAT1/serial_number"
    value = read(FILE_PATH)
    return value

def technology():
    FILE_PATH = "/sys/class/power_supply/BAT1/technology"
    value = read(FILE_PATH)
    return value

def gettype():
    FILE_PATH = "/sys/class/power_supply/BAT1/type"
    value = read(FILE_PATH)
    return value