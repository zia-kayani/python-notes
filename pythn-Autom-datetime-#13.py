#STRFTIME  -- is used to create your own datetime format
            #create string representation of datetime object
# %y -- year ,    %m -- month   %d -- day,  %H -- hour ,    %M -- minutes,  %S -- Seconds

import datetime

current=  datetime.datetime.now()
print(current)
print(type(current))

year =  current.strftime("%y")
print("my year is ", year)
print(type(year))

month = current.strftime("%m")
print("my month is ", month)
print(type(month))

day =  current.strftime("%d")
print("my day is ", day)
print(type(day))

time =  current.strftime("%H : %M : %S")
print("my time is ",  time)
print(type(time))

date_time =  current.strftime("%y - %m - %d ")
print(date_time)

date_time =  current.strftime("%y/%m/%d ")
print(date_time)

date_time =  current.strftime("%d/%m/%y - %H:%M:%S ")
print(date_time)
print(type(date_time))

#we can also do like this

from datetime import datetime as dt
current=dt.now()
print(current)



from datetime import datetime as dt
current=dt.now()
#print(current)


current=current.strftime('%A %m %y')
print(current)



#custom date tim e ---------------
from datetime import datetime
current= datetime.now()
print(current)
type(current)

custom_date =  datetime.strftime(current , "%y/%m/%d")
print(custom_date)
print(type(custom_date))

custom_date_time =  datetime.strftime(current , "%d/%m/%y : %H-%M-%S %p") #%p shows pm /am
print(custom_date_time)


#------------- STRPTIME -------------
#if you need to convert string to date obbject we use strptime 
# STRFTIME VS STRPTIME 
# STRFTIME --> date to string 
# STRPTIME --> String to date


from datetime import datetime
mydate='2022/09/05 13:20:52'
print(type(mydate))
#now convert str fromat to datetime formate
myptime= (datetime.strptime(mydate,"%Y/%m/%d %H:%M:%S"))
print(myptime)
print(type(myptime))


# --------------------- TIME   ----------------
import time
seconds =  time.time()
print(seconds)  #this will show time in sha seconds like : 1746091553.9320002

#in order to convert this shaw time to proper time we hv two methods
#1 method
import datetime
import time
seconds = time.time()
print(datetime.datetime.fromtimestamp(seconds)) #this will convert sha time to proper time

#2nd time
import time
seconds = time.time()
local_time  = time.ctime(seconds)
print(local_time)
print(type(local_time))


#we can get our gmtime
mygmt =  time.gmtime()
print(mygmt)

#we can see localtime
mylocalt= time.localtime()
print(mylocalt)

#we can also use strftime with time module
myvr= time.strftime("%y - %m - %d")
print(myvr)

#we can also set sleep timer for execution break like
print("hello from zia kayani kashmiri ")
time.sleep(2)
print("message after 2 seconds ")
time.sleep(4.2)
print("final message")


#to check for creation time of a file 
import os
import datetime
# myfile =  os.path.getctime("/home/zia/Documents/zia.tx")
myfile =  os.path.getctime("e:\Web Development\python learning\pythn-Autom-datetime-#13.py")
print(myfile)


myfile =  os.path.getctime("e:\Web Development\python learning\pythn-Autom-datetime-#13.py")
print(datetime.datetime.fromtimestamp(myfile))


#to search for a file 


import os
import datetime

find_file=input("Enter the search:")

for roots,dirs,files in os.walk("e:\Web Development\python learning\ "):
    for i in files:
        if i==find_file:
            print("Yes we have files as per your find request",i)

#search for desired file and show creation time as well 
import os
import datetime
find_file = input("enter your file name")
for roots,dirs,files in os.walk("e:\Web Development\python learning\ "):
    for i in files:
        if i == find_file:
            print("your file is this ", i)
            mypath=  os.path.join(roots, i)
            print("your whole file path is this ", mypath)
            print("your file creation time is this " , datetime.datetime.fromtimestamp(os.path.getctime(mypath)))

#TASK TIME --->
# Search the file from your path and find time as per below format :-
# Date is : September 10 2022 Time is : 10:12:35 PM 

import os 
import datetime

find_file = input("Enter the name of the file to find: ")
for roots, dirs, files in os.walk(r"e:\Web Development\python learning"):
    for f in files:
        if f == find_file:
            filepath = os.path.join(roots, f)
            filectime = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
            print("Date is: " + datetime.datetime.strftime(filectime, "%m-%d-%y") +
                  " Time is: " + datetime.datetime.strftime(filectime, "%H:%M:%S"))
