# Start pip installation
if pip install -r requirements.txt; then
    # Display completion message in green
    echo -e "\033[0;32m\nSetup Complete\033[0m"
    
    # Pause for 1 second
    sleep 1
    
    # Display prompt message in yellow
    echo -e "\033[0;33m\nPress Enter to continue... \033[0m"
    
    # Read user input
    read -r
    
else
    # Display error message in red
    echo -e "\033[0;31m\nFailed to install modules.\033[0m"
    sleep 1                                                      # Exit with non-zero status to indicate failure

fi
