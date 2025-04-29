#os path  ----------

#basename and dirname 
#basename is used to see the current filename
#dirname is used to see the current working dir


#!/usr/bin/python

import os
mypath="/home/zia/Documents/python_prac/test.py"

print(f"my base path is : {os.path.basename(mypath)}")
print(f"my directory is {os.path.dirname(mypath)}")

#path.split
#split is used to split the result 
splittedvar= os.path.split(mypath)
print(splittedvar)
print(f"my base path is  {splittedvar[1]}")
print(f"my directory path is  {splittedvar[0]}")

#isfile and isdir
#isfile/isdir is used to verify if path is file/direcotry
print(os.path.isfile(mypath))
print(os.path.isdir(mypath))

if os.path.isfile(mypath):
    print("this is file")
else:
    print("this is directory")

mypath1="/home/zia/Documents/python_prac" #now directory path
if os.path.isdir(mypath1):
    print(f"this is dir path: {mypath1}")
else:
    print(f"this is not dir path: {mypath1}")

#isexist  
if os.path.exists(mypath1):
    if os.path.isdir(mypath1):
        print(f"this is directory path : {mypath1}")
else:
    print(f"path is not valid {mypath1}")

#islink
if os.path.islink(mypath1):
    print(f"this is link path {mypath1}")
elif os.path.isfile(mypath1):
    print(f"this is file path {mypath1}")
else:
    print(f"thiis is directory path {mypath1}")


#join
p1="/home/zia/Documentes"
p2="/test.py"
joinedpath=os.path.join(p1+p2)
print(f"whole path is : {joinedpath}")

#sep
print(os.path.sep)

#getsize 
print(os.path.getsize(mypath)) #will show size in bytes

#normpath  
newpath="//home//zia/Desktop"
print(newpath)
print(os.path.normpath(newpath)) #normpath is used to remove extra spces

#normcase
p22="/Home/Zia/kiani/ali.txt"
print(p22)
print(os.path.normcase(p22))

#samefile
file1="/home/zia/zia.txt"
file2="/home/zia/kiani.txt"
print(os.path.samefile(file1, file2))




#Task - 
# 1-  show memory info as below
    #total memory is :3 gB
    #used memory is :  12 GB
    #swap memory is : 0 GB
# 2-  storage details
    # root directory name is : /
    # root directory total size is : 44 GB
    # Root directory used size is : 8 GB

#!/usr/bin/python
import os
#solution task#1
free_output = os.popen(" free -g" ).read()

lines = free_output.strip().splitlines()
for line in lines:
    if line.startswith("Mem:"):
        parts = line.split()
        total_memory = parts[1]
        used_memory = parts[2]
        print(f"Total memory is : {total_memory} GB")
        print(f"Used memory is  : {used_memory} GB")


#task2 solution -- to check storage details
output = os.popen("df -h").read()
lines =  output.strip().splitlines()
print(lines[4])
line4=lines[4]
splitres= line4.split()
print(type(splitres))
print(f"root directory is {splitres[5]}")
print(f"total memory is = {splitres[1]}")
print(f"used memroy is = {splitres[2]}")
