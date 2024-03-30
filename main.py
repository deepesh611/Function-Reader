# A simple program to display all the functions of a module along with their docstrings.


# Importing the required modules
import lib
import time
import pyfiglet as fig
from colorama import Fore


# Main Program

base1 = "https://docs.python.org/3/library/"
base2 = "https://pypi.org/project/"

for i in fig.figlet_format("FUNCTION - READER" ,font = 'big', width = 200).split('\n'):
    print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.GREEN)

while True:
    module_name = input(Fore.LIGHTGREEN_EX + '\nEnter Module Name without Extension (if any):\n' + Fore.RESET)

    if not module_name:
        print(Fore.RED + 'Please Enter a Valid Module Name' + Fore.RESET)
        
    else:
        lib.list_functions(module_name)
            
            # try:
            #     print(Fore.LIGHTCYAN_EX + f"\nOpening the Official Documentation of {module_name} in the Browser..." + Fore.RESET)
            #     time.sleep(1)
            #     lib.run_command(['start', command])
            
            # except FileNotFoundError:
            #     try:
            #         command = base1 + module_name + ".html#module-_" + module_name
            #         lib.run_command(['start', command])
            #     except:
            #         try:
            #             command = base1 + module_name + ".html#module-__" + module_name
            #             lib.run_command(['start', command])
            #         except:
            #             command = base2 + module_name
            #             lib.run_command(['start', command])
            
            # except:
            #     print(Fore.RED + "Failed to Open the Documentation in the Browser." + Fore.RESET)
        
        
    n = input('\nFind for More Modules? (y/n): ')                         
    if n.lower() != 'y':
        break





# abc.html#module-abc