import os
import subprocess
from hadoop import hadoopStart
from aws import awsStart
from docker import dockerStart
def clearscr():
    x = subprocess.getstatusoutput("cls")
    if x[0] == 0:
        os.system("cls")
    else:
        os.system("clear")
def startmsg():
    clearscr()
    print("                 Menu Program                      ")
    print("---------------------------------------------------\n")
def start():
    startmsg()
    while True:
        print("""    Enter
        1. For Hadoop
        2. For Amazon Web Services
        3. For Docker
        4. exit
        => """,end = "")
        choice = input()
        startmsg()
        if choice == '1':
            hadoopStart()
            startmsg()
        elif choice == '2':
            awsStart()
            startmsg()
        elif choice == '3':
            dockerStart()
            startmsg()
        elif choice == '4':
            break
        else:
            print("Please enter correct choice....")
    clearscr()
start()