#!/bin/bash

# Change directory to src
cd ./src || return 1

# Function to run the Python script
run_script() {
    local python_cmd=$1
    if command -v $python_cmd &> /dev/null; then
        $python_cmd ./main.py
        return 0
    else
        return 1
    fi
}

# Try to run the script with python
if run_script python; then
    echo "Script executed with python."
elif run_script python3; then
    echo "Script executed with python3."
else
    echo "Error: Neither 'python' nor 'python3' is available on this system."
    exit 1
fi

