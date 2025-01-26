#Libs
import os
import sys
import socket
import time

def info():
    global target
    global targetip
    global myip
        
    target = sys.argv[1]
    targetip = socket.gethostbyname(target)
    myip = socket.gethostbyname(socket.gethostname())