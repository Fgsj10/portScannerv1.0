"""
Creating one project about port scanner
In computer network, this is version 1.0
----------------------------------------
Author = Francisco Junior
"""

#Importing libraries
import socket
import subprocess
import sys
from datetime import datetime
import platform

#----------------------------------------
#Cleaning of screen
if platform.system() == "Windows":
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)


#Ask for input
remoteServer   = str(input("Enter with remote host for scan: "))
remoteServerIP = socket.gethostbyname(remoteServer)

#Print nice banner with information on which host
print("-") * 60 #Why multiplication for 60?

print("Please wait, scanning remote host", remoteServerIP)

print("-") * 60 #Why equal question

#Checking of time of scanning
t1 = datetime.now()


#using try and catch for treatment exception
try:
    for port in range(1,1025):
        sock   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP), port)
        if result == 0:
            print("port {}: OPEN".format(port))
        sock.close() #End connection


except KeyboardInterrupt:
    print("Press CTRL+C")
    sys.exit()

except socket.gaierror:
    print("hostname could not be resolved. Exiting")

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

#Checking time again 
t2 = datetime.now()


#Calculating total time
total = t2 - t1


#Printing information of scanner in screen

print("Scanning complete in: ", total)