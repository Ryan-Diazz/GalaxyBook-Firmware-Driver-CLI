#!/usr/bin/env python3

import argparse
import importlib
import pkgutil
import galaxybook.commands as commands_pkg
from galaxybook.utils import require_root


def loadCommands(subparsers):
    """
    Automatically load all command plugins.
    """
    package_path = commands_pkg.__path__

    for _, module_name, _ in pkgutil.iter_modules(package_path):
        module = importlib.import_module(
            f"galaxybook.commands.{module_name}"
        )

        if hasattr(module, "register"):
            module.register(subparsers)

def main():
    parser = argparse.ArgumentParser(prog="galaxybook")
    subparsers = parser.add_subparsers(dest="command")

    loadCommands(subparsers)

    # # recording command
    # record_parser = subparsers.add_parser("recording")
    # record_parser.add_argument(
    #     "action",
    #     choices=["show", "toggle", "on", "off"]
    # )

    # #powerlid command
    # lid_parser = subparsers.add_parser("powerlid")
    # lid_parser.add_argument(
    #     "action",
    #     choices=["show", "toggle", "on", "off"]
    # )

    args = parser.parse_args()

    if getattr(args, "requires_root", False):
        if hasattr(args, "action") and args.action != "show":
            require_root()
    
    if hasattr(args, "func"):
        args.func(args)
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()