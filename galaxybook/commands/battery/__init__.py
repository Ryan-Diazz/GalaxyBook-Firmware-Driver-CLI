from . import limit, health, status, wattage, info

def register(subparsers):
    parser = subparsers.add_parser(
        "battery",
        help="Manage battery features"
    )
    # Nested subparsers for battery subcommands
    battery_parsers = parser.add_subparsers(dest="battery_commands")
    
    # Import and register each battery subcommand
    info.register(battery_parsers)
    status.register(battery_parsers)
    health.register(battery_parsers)
    limit.register(battery_parsers)
    wattage.register(battery_parsers)
    
    
    # Show help if no subcommand is given
    parser.set_defaults(func=lambda args: parser.print_help())
