from galaxybook.utils import read, write, perm
import time
import os

# ------------------
# register command
# ------------------
def register(subparsers):
    parser = subparsers.add_parser(
        "wattage", 
        help="monitor system wattage"
    )

    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=1.0,
        help="Refresh rate in seconds"
    )

    parser.set_defaults(func=handle)

# ------------------
# handler
# ------------------

def handle(args):
    monitor(args.interval)

# ------------------
# command implementation
# ------------------

def monitor(interval):
    min_w = float("inf")
    max_w = 0
    total_w = 0
    samples = 0

    try:
        # hide cursor
        print("\033[?25l", end="")

        print("Battery Power Monitor".center(40, "-"))
        print()  # space for dynamic content
        print()
        print()
        print()
        print("-" * 40)
        print("Press Ctrl+C to exit.")        
        
        while True:
            voltage = voltage_now() / 1_000_000
            current = current_now() / 1_000_000
            wattage = voltage * current

            min_w = min(min_w, wattage)
            max_w = max(max_w, wattage)
            total_w += wattage
            samples += 1
            avg_w = total_w / samples

            # move cursor up to overwrite values
            print("\033[6F", end="")

            print(f"{'Current:':20} {wattage:.2f} W")
            print(f"{'Minimum:':20} {min_w:.2f} W")
            print(f"{'Maximum:':20} {max_w:.2f} W")
            print(f"{'Average:':20} {avg_w:.2f} W")
            print("-" * 40)
            print("Press Ctrl+C to exit.")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\033[?25h", end="")
        print("\nExiting wattage monitor...")


def voltage_now():
    FILE_PATH = "/sys/class/power_supply/BAT1/voltage_now"
    value = read(FILE_PATH)
    return float(value)

def current_now():
    FILE_PATH = "/sys/class/power_supply/BAT1/current_now"
    value = read(FILE_PATH)
    return float(value)