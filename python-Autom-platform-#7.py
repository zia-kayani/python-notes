#platform module --is similer like a uname in linux 
#it will show system related information 
#like we do in linux 
# uname -a #all system related information 
# uname   #platform
# uname -m #architecture 
# unmae -r #kernal information 


#windows
import platform
print(platform.system())

#platfrom.processor()
print(platform.processor())

#platform.architecture()
print(platform.architecture())

#platfrom.node
print(platform.node()) #show machine name 


#platform.platform
print(platform.platform()) #shows platform infrmation

#platfrom.machine
print(platform.machine()) #shows processor type like AMD64 or intel etc

#platfrom.uname
print(platform.uname()) #shows all info including system, node, releasem versin etc

#platform.release()
print(platform.release())

#now wrring a python script which is platfrom independent 
import os 
if platform.system() == "Windows":
    os.system("ipconfig")
elif platform.system() == "Linux":
    os.system("ifconfig")
else:
    print("sorry, please check with admin ")