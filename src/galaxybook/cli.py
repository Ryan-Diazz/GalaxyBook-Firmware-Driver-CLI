#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete
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

    argcomplete.autocomplete(parser)

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