# #python mdules ------------------
# # sometime you write some code and want to use that in seperate files so we can 
# # use that file as a module

# # there are three types of modules
# # 1- user defined
# # 2- built in modules
# # 3- third party modules

# #user defined module 
# #myfile.py
# fname="zia"

# #otherfile.py
# import myfile
# print(myfile.fname)

# #or we can import
# from myfile import *
# print(fname)

# #or we can 
# import myfile as zee
# print(zee.fname)

# #built in modules
# import os 
# os.system("dir")

# os.system("ipconfig")
# dir(os) #for ethernet adapter check

# #third party modules 
# #we can install third party modules like pandas , sleenium ,etc etc

# #--------------OS module---
# import os 
# print(os.getcwd())

# #to  see the current direcorty and change that 
# print(os.getcwd())
# dir_path ="c:\\users" #linux - /home/zia etc
# os.chdir(dir_path)
# print(os.getcwd())


# #to list the current directories
# print(os.listdir()) #will show the working directories in currect path

# # to see the seperator 
# print(f"my windows seperator is {os.sep}")


# #to make direcory
# os.mkdir("zain")
# print(os.listdir())

# #to remove the dir
# os.rmdir("c:\\users\zain")
# print(os.listdidr())

# #to rename or remove the file 
# os.rename("zian", "zia")
# print(os.listdir())

# #process , group and user ids  in linx
# print("my currnt working dir is", os.getcwd())
# print("my user is id : ", os.getuid())
# print("my group id is ", os.getgid())
# print("my process id is : ", os.getpid())

# #Task -- show only .txt file in current work dir in linux /windows
# dir_name =os.getcwd()
# for filename in os.listdir(dir_name):
#     if filename.endswith(".txt"):
#         print(filename)



#---walk command in os module 
#is used to see the directories and files inside it
import os 
print(list(os.walk(os.getcwd())))

#in order to read the system info and save to variable 
#we use popen and read commands
val =  os.system("ipconfig")
print(" val data :" , val) #this will not show any output but 0 or 1 
                            #data is not saved , for this popen read command use
mydata= os.popen("ipconfig").read()
print(mydata)

#task -  show current os version like i 22.04,4.LTS
#use two way
#1st -- with linux like with awk command etc
#2nd -- with python only 

#in python 
import os
mylist= list(os.uname())
print(mylist[2])

#in linux
#uname -a | awk '{print $3}'


