# Scripted by Samay
# Simple as Fu#ck

# ---------------- Imports
import os
import shutil

try:
    import pyzipper
    import colorama
except ImportError:
    _ = os.system('pip install colorama' if os.name == 'nt' else 'pip3 install colorama')
    _ = os.system('pip install pyzipper' if os.name == 'nt' else 'pip3 install pyzipper')
    _ = os.system('pip install requests' if os.name == 'nt' else 'pip3 install requests')
import pyzipper
import sys
from time import sleep
from getpass import getpass
from colorama import Fore
os.system('pip install progress')
# -------------------Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

# ------------------banners
logo = Fore.RED + """
  ___________________________________ _____________ 
 /   _____/\_   _____/\__    ___/    |   \______   |
 \_____  \  |    __)_   |    |  |    |   /|     ___/
 /        \ |        \  |    |  |    |  / |    |    
/_______  //_______  /  |____|  |______/  |____|    
        \/         \/                              
            """ + Fore.YELLOW + """>>> """ + Fore.GREEN + """Zork X Kdo""" + Fore.YELLOW + """ <<< 

"""


def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def exixting_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def designprint(samaywrite):
    print(r+"└─> "+w+"\033[1;37m"+samaywrite)

def front_design():
    cls_clear_func()
    banner()

front_design()


class Setup:
    def __init__(self,user):
        self.data = user
    def mainFile(self):
        self.save = self.data
        try:
            with pyzipper.AESZipFile('Configs/ngl.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.extractall(pwd=str.encode(self.save))
            designprint('Password Correct !')
            sleep(2.3)
            front_design()
            designprint('Successfully Decrypted and unzipped file with password..')
            sleep(3.0)
            exixting_directory_file('Configs/ngl.zip')
            cls_clear_func()
            banner()
            with open('run.py','w') as fie:
                fie.write('''
import os
if os.name == 'nt':              
    os.system('node function.js')
else:
    os.system('bash run.sh')
                ''')
            if os.name == 'nt':
                os.system('npm install')
                designprint('Successfully installed npm packages now run the script python run.py')
                sleep(2.3)
                __import__('os').remove(__import__('os').path.realpath(__file__))

                
                
            else:
                os.system('bash run.sh')
                __import__('os').remove(__import__('os').path.realpath(__file__))

        except Exception as samay:
            designprint('Password Incorrect !')
            sleep(0.5)
            os.system('python main.py' if os.name=='nt' else 'python3 main.py')


try:
    user_ezip_unzipping = getpass(r+"└─"+w+"\033[1;37mEnter the password of Zipfile : "+r).strip()
except:
    pass

if __name__ == '__main__':
    # exixting_directory_file('main.py')
    main_start = Setup(user_ezip_unzipping)
    main_start.mainFile()