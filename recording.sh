#!/bin/bash

# the beginning and escalation :P

# Path to the block recording attribute
FILE="/sys/class/firmware-attributes/samsung-galaxybook/attributes/block_recording/current_value"

# Function to read the current value
show_current() {
    current=$(cat "$FILE")
    if [ "$current" = "1" ]; then
        echo "Recording Block: ON"
    else
        echo "Recording Block: OFF"
    fi
}

# Function to set value (0=ON, 1=OFF)
set_value() {
    value=$1
    echo "$value" | sudo tee "$FILE" > /dev/null
    show_current
}

# Function to toggle value
toggle_value() {
    current=$(cat "$FILE")
    if [ "$current" = "0" ]; then
        set_value 1
    else
        set_value 0
    fi
}

# Main command handling
case "$1" in
    toggle | t | TOGGLE | T)
        toggle_value
        ;;
    on | ON)
        set_value 1
        ;;
    off | OFF)
        set_value 0
        ;;
    show)
        show_current
        ;;
    *)
        echo "Usage: $0 [show|toggle|on|off]"
        exit 1
        ;;
esac