# A simple program to display all the functions of a module along with their docstrings.


# Importing the required modules
import src.lib as lib
import time
import pyfiglet as fig
from colorama import Fore, Style


# Main Program

base1 = "https://docs.python.org/3/library/"
base2 = "https://pypi.org/project/"

print()

for i in fig.figlet_format("FUNCTION - READER" ,font = 'big', width = 200).split('\n'):
    print(Fore.LIGHTMAGENTA_EX + i.center(120))

print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '\nYou can give \'q\' as input to quit the program at any time.\n' + Style.RESET_ALL)
time.sleep(1)

while True:
    module_name = input(Fore.LIGHTGREEN_EX + '\nEnter Module Name without Extension (if any):\n' + Fore.RESET)

    if module_name.lower() != 'q':
        
        if not module_name:
            print(Fore.RED + 'Please Enter a Valid Module Name' + Fore.RESET)
            
        else:
            print(Fore.LIGHTYELLOW_EX + '\n  Loading Functions...\n' + Fore.RESET)
            lib.list_functions(module_name)
    
    else: 
        print()
        quit()
