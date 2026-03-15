import os
import sys

def require_root():
    if os.geteuid() != 0:
        cmd = os.path.basename(sys.argv[0])
        print("This command must be run as root!")
        print(f"Try: sudo {cmd} {' '.join(sys.argv[1:])}")
        sys.exit(1)