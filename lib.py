
# Importing Required Libraries
import time
import requests
import importlib
import subprocess
from colorama import Fore, Style



# TO RUN A COMMAND IN POWERSHELL
def run_command(cmd):    
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.returncode, result.stdout
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stderr
    
    

# Function to list all the functions of a module along with their docstrings
def list_functions(module_name):
    try:
        module = importlib.import_module(module_name)
        all_attributes = dir(module)
        functions_list = [attribute for attribute in all_attributes if callable(getattr(module, attribute))]

        print(Fore.LIGHTMAGENTA_EX + "\n======= LIST OF ALL FUNCTION =======\n" + Fore.RESET)
        time.sleep(1)

        for i, function_name in enumerate(functions_list, start=1):
            print(str(i)+'.')
            function = getattr(module, function_name)
            docstring = function.__doc__ if function.__doc__ else "No docstring available."
            print(f"{Fore.YELLOW}{Style.BRIGHT}Function: {function_name}{Fore.RESET}{Style.RESET_ALL}\n\n{docstring}\n\n")
            time.sleep(0.01)
            
        time.sleep(1)
        print(Fore.GREEN + "======= END OF FUNCTION LIST =======\n" + Fore.RESET)
        
        view_docs(module_name)

    except ModuleNotFoundError:
        print(Fore.RED + '\nModule Not Found\nPlease Enter a Valid Module Name and Make sure that you have Installed that Library.' + Fore.RESET)
        
    except AttributeError:
        print(Fore.RED + '\nAttributeError: The given module does not contain any callable attributes.' + Fore.RESET)



# Function to validate a URL
def validate_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:                             # URL is valid and accessible
            return True
        else:
            return False                                            # URL is valid but returns an error (e.g., 404)
    except requests.exceptions.RequestException:
        return False                                                # URL is invalid or inaccessible
    
    
    
# Function to view the official documentation of a module in the browser
def view_docs(module_name):
    base1 = "https://docs.python.org/3/library/"
    base2 = "https://pypi.org/project/"
    
    try:
       if input("\nDo you want to see the Official Documentation of this Module? (y/n): ").lower() == 'y':        
            command1 = base1 + module_name + ".html#module-" + module_name
            command2 = base1 + module_name + ".html#module-_" + module_name
            command3 = base1 + module_name + ".html#module-__" + module_name
            command4 = base2 + module_name + '/'
            
            if validate_url(command1):
                print(Fore.LIGHTCYAN_EX + f"\nOpening the Official Documentation of {module_name} in the Browser..." + Fore.RESET)
                run_command(['start', command1])
            
            elif validate_url(command4):
                print(Fore.LIGHTCYAN_EX + f"\nOpening the Official Documentation of {module_name} in the Browser..." + Fore.RESET)
                run_command(['start', command4])
            
            elif validate_url(command2):
                print(Fore.LIGHTCYAN_EX + f"\nOpening the Official Documentation of {module_name} in the Browser..." + Fore.RESET)
                run_command(['start', command2])
            
            elif validate_url(command3):
                print(Fore.LIGHTCYAN_EX + f"\nOpening the Official Documentation of {module_name} in the Browser..." + Fore.RESET)
                run_command(['start', command3])
            
            else:
                print(Fore.RED + "Failed to Open the Documentation in the Browser." + Fore.RESET)
    
    except:
        print(Fore.RED + "Failed to Open the Documentation in the Browser." + Fore.RESET)
    
    
    
