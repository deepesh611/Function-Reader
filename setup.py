import time
import subprocess
import threading
import sys


def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return process.returncode, output + error


def loading_animation():
    l = r'/-\|'
    while not installation_complete:
        for i in l:
            print('Installing Required Libraries ' + i, end='\r', flush=True)
            time.sleep(0.1)
            sys.stdout.write("\033[K")


def install_libs():
    global installation_complete
    installation_complete = False

    try:
        # Start the loading animation in a separate thread
        loading_thread = threading.Thread(target=loading_animation)
        loading_thread.start()

        return_code, output = run_command('pip install -r ./requirements.txt')

        if return_code == 0:
            print(f"\nCommand 'pip install -r ./requirements.txt' executed successfully.\n\n{output}")
        else:
            print(f"\nError: Command 'pip install -r ../requirements.txt' failed with return code {return_code}. Output:\n{output}")
            time.sleep(5)
            exit()

    except Exception as e:
        print(f'\nError in installing required libraries: {str(e)}\nPlease refer to the README file for manual installation of libraries.\n')
        time.sleep(6)
        exit()

    finally:
        # Signal that the installation is complete
        installation_complete = True
        # Wait for the loading thread to finish
        loading_thread.join()


print('\n\n',time.ctime(),'\n')
install_libs()
time.sleep(2)

from colorama import Fore

print(Fore.GREEN + 'Modules Installed Successfully...')
time.sleep(1)
print('Setup Completed...\n' + Fore.RESET)
input('Press Enter to Exit...')
