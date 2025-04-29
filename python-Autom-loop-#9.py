#Loops are important which help us to do repeated tasks 

print(list(range(1,11)))
print(list(range(0,11,2))) #will increment by 2

myl =['zia', 'kiani', 'kashmiri']
for i in myl:
    print(i)

a,b,c=1,22,44
print(a , b ,c)

val={"name":"zia" , "country":"kashmir"}
for k, v in val.items() :
    print(k)

for k in val.keys():
    print(k)

for v in val.values():
    print(v)

#while --condition
vv=10
while 0 <= vv:
    print("hi")
    vv=vv-1




#!/usr/bin/python
import os

#print(list(os.walk(os.getcwd())))
for roots,dirs,files in list(os.walk(os.getcwd())) :
   print(roots)
   print(dirs)
   print(files)
   print(len(files))


#to show the directoreis which are not empty 
for roots,dirs,files in list(os.walk(os.getcwd())):
    if len(files) !=0:
        print(roots)
        for i in files:
            print(i)

#to see the full path of dirs with files - which  dirs are not empty             
for roots,dirs,files in list(os.walk(os.getcwd())):
    if len(files) !=0:
        print(roots)
        for i in files:
            print(os.path.join(roots,i))

#task -1    how to find txt file in python (both on linux and windows)
#task -2  i want to creat like find command in linux , if you search any file with user defined 
        #variable then it should be find from your current  directory or from root
        # example:  find /root/lect23/  -name testing.csv
            #/root/lect23/test/testing.csv




#!/usr/bin/python
#first task
import os
for roots,dirs,files in list(os.walk(os.getcwd())):
    if len(files) !=0:
        for i in files:
            if i.endswith(".txt"):
                print(i)
#second task:
import os
import sys
tofind=sys.argv[1]
for roots, dirs, files in list(os.walk(os.getcwd())):
    if len(files) != 0:
        for i in files:
            if tofind == i:
                print(i)


