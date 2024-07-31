from colorama import Fore, Style, init
# import subprocess
import pyfiglet
init()

PINK = '\033[38;2;255;105;180m'
RESET = Style.RESET_ALL
text = pyfiglet.figlet_format("Jonh Tool")
print(PINK + text + RESET)

print(PINK +"=====[Wellcome Jonh Tool]===== "+ RESET)
Text = input(PINK+'Input text or number to print :'+RESET)
i = int(input(PINK+"Input number :"+RESET))
counter = 0
while counter<i:
    print(PINK+f" {Text}" + RESET)
    counter+= 1
else:
    print(Fore.BLUE+"Successfull !")

# subprocess.call("ifconfig"+ i , shell=True)