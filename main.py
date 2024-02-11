# A simple program to display all the functions of a module along with their docstrings.


# Importing the required modules
import importlib
import time
import pyfiglet as fig
from colorama import Fore, Style


# Function to list all the functions of a module along with their docstrings
def list_functions(module_name):
    try:
        module = importlib.import_module(module_name)
        all_attributes = dir(module)
        functions_list = [attribute for attribute in all_attributes if callable(getattr(module, attribute))]

        print(Fore.LIGHTMAGENTA_EX + "\n===== LIST OF ALL FUNCTION NAMES =====\n" + Fore.RESET)
        time.sleep(1)

        for i, function_name in enumerate(functions_list, start=1):
            print(str(i)+'.')
            function = getattr(module, function_name)
            docstring = function.__doc__ if function.__doc__ else "No docstring available."
            print(f"{Fore.YELLOW}{Style.BRIGHT}Function: {function_name}{Fore.RESET}{Style.RESET_ALL}\n\n{docstring}\n\n")
            time.sleep(0.01)
            
        time.sleep(1)
        print(Fore.GREEN + "======= END OF FUNCTION LIST =======\n" + Fore.RESET)

    except ModuleNotFoundError:
        print(Fore.RED + '\nModule Not Found\nPlease Enter a Valid Module Name and Make sure that you have Installed that Library.' + Fore.RESET)
        
    except AttributeError:
        print(Fore.RED + '\nAttributeError: The given module does not contain any callable attributes.' + Fore.RESET)





# Main Program

for i in fig.figlet_format("FUNCTION - READER" ,font = 'big', width = 200).split('\n'):
    print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.GREEN)

while True:
    module_name = input(Fore.LIGHTGREEN_EX + '\nEnter Module Name without Extension (if any):\n' + Fore.RESET)

    if not module_name:
        print(Fore.RED + 'Please Enter a Valid Module Name' + Fore.RESET)
    else:
        list_functions(module_name)

    n = input('\nFind for More Modules? (y/n): ')                           # Asking if user wants to continue or quit
    if n.lower() != 'y':
        break
