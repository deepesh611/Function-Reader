#!/bin/bash

# ANSI color codes
green='\033[0;32m'
yellow='\033[1;33m'
reset='\033[0m' # Reset to default color

# Start pip installation
if pip install -r requirements.txt; then
    # Display completion message in green
    echo -e "\n${green}Modules installed successfully.${reset}"
    sleep 1
    # Prompt user to continue in yellow
    echo -e "\n${yellow}Press Enter to continue...${reset} "
    read
else
    # Display error message in red
    echo -e "\n${red}Error: Failed to install modules. Please check the requirements file and try again.${reset}"
    exit 1
fi
