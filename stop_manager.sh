#!/bin/bash

# Find the process ID (PID) of the Python process
pid=$(pgrep -f "python3 bot_manager.py")

# Check if the process is running
if [ -n "$pid" ]; then
    # If the process is running, kill it
    kill "$pid"
    echo "Process stopped."
else
    echo "Process is not running."
fi