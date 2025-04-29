#sys module
#is used to manipulate commmand line arguments
#used for python runtime environments as like interpretter

import sys
print(sys.version)

#version information
print(sys.version_info)

#sys path
print(sys.path)

#sys exit -- to exit running further code in terminal
print("zia ")
# sys.exit()
print("after exit ") #this will not run bcz ,terminal exited before

#argv -- to see the arguments passed from console 
print(sys.argv)

#arguments are passed like
    # in linux  -->  ./myfile.py abd1 abd2 
    #in windows -->   python myfile.py abd1 abd

#total arguments
#by default one arguments is passed which is filename of itself 
#so there will be one argument always
print(len(sys.argv))

#see the second argument passed 
print(sys.argv[1]) 

print("this is script name" + str(sys.argv[0]))
print("my full arguments are "+ str(sys.argv))
print("my total arguments are "+ str(len(sys.argv)))


import os
import sys
print(os.system("systemctl status sshd"))

action= input("enter the action for sshd service")
os.system(f"systemctl {action} sshd")

#to only allow 2 arguments one is bydefault and one is you pass
if len(sys.argv) !=2:
    print(f"you have to pass at least one argument for command : systemctl {sys.arg[1]} sshd: exmple status,start,restart")
    sys.exit()
else:
    action=sys.argv[1]
    os.system(f"systemctl {action} sshd")
