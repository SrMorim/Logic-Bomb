#!/usr/bin/env python3
#-=Libs=-
import os
import sys
import socket
import time

#-=Imports=-
from attack import *
from defense import *
from utils import *

#-=Menus=-
#Main Menu
def mainmenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
           __             _         ___             __ 
          / /  ___  ___ _(_)___    / _ )___  __ _  / / 
         / /__/ _ \/ _ `/ / __/   / _  / _ \/  ' \/ _ \\
        /____/\___/\_, /_/\__/   /____/\___/_/_/_/_.__/
                  /___/                                  
       -===============================================-
        𝑻𝒂𝒓𝒈𝒆𝒕:{target}
        𝑻𝒂𝒓𝒈𝒆𝒕 𝑰𝑷:{targetip}
        Your IP:{myip}
        ''')
        option = str(input("[1]Defense\n[2]Attack\n[3]New Target\n[x]Exit\n>>> "))

        if option == "1":
             defensemenu()
             break
        elif option == "2":
             attackmenu()
             break
        elif option == "3":
             newtarget()
        elif option == "x":
            break



if __name__ == "__main__":
    #Required
    info()

    #Start
    mainmenu()

    
