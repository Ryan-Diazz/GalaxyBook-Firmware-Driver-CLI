"""
Commands for galaxybook CLI.

Each module should implement:

    def register(subparsers):
        parser = subparsers.add_parser("command name")
        parser.add_argument("action", choices=["show", "toggle", "on", "off"])
        parser.set_defaults(func=handle)

and:
    def handle(action):
        ...


The CLI automatically discovers modules in this package.
"""