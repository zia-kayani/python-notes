#--------JSON ---------------
#JSON is a javascript object notatoin 
#it is a data formate for structure data

with open('myjson.json') as file:
    print(file.read())

#how to convert json to dictionary format 
# jsonfile =  "E:\Web Development\python learning\myjson.json"
# with open(jsonfile , 'r') as file:  
#     my_dict =  json.load(file) #this will cause an error , as we have to import json first
#     print(my_dict)

import json
jsonfile =  "E:\Web Development\python learning\myjson.json"
with open(jsonfile , 'r') as file:  
    my_dict =  json.load(file) #this will cause an error , as we have to import json first
    print(my_dict)


#to access specific value from dictionary
print(my_dict['name'])

#to run loop on json file 
for i in my_dict:
    print(i) #this will show only keys of dictionary

#to show both keys and values
for k,v in my_dict.items():
    print(f"key is: {k} && value is :{v}")

##################

jsonfile =  "E:\Web Development\python learning\os.json"
with open(jsonfile,"r") as jf:
    my_dict= json.load(jf)
   #print(my_dict)

for i in my_dict:
    #print(f"My dictionary is {i}")
    for k,v in i.items():
        print(f"My key is {k}")
        print(f"My value is {v}")

#to see specific value based on condition
with open(jsonfile,"r") as jf:
    my_dict= json.load(jf)
    #print(my_dict)

for i in my_dict:
    #print(i)

    for k,v in i.items():
        if v == 'Ubuntu':
            print("My Ubuntu version is ", i["Version"])
        if v == 'CentOS':
            print("My CentOS version is ",i['Version'])


#How to convert dictionary to JSON data 
myinfo = {
	"server1" : { 
		"IBM": {
			"datacenter":"Bangalore",
			"env": {
				"PR": "192.168.1.1",
				"DR": "192.168.1.2"
				}
			}
		    }
	}
print(myinfo)
mypath="user_details.json"
with open(mypath,'w') as df:
    json.dump(myinfo,df)



print(type(myinfo))


#. ........................ .
mypath="user_details.json"
with open(mypath,'w') as df:
    json.dump(myinfo,df,indent=4) #it gives 4 spaces as an indentation spaces
#. ..................... .



#######TASK TIME#######################

mylist= [
  {
    "name": "apple",
    "color": "green",
    "price": 1.2
  },
  {
    "name": "banana",
    "color": "yellow",
    "price": 0.5
  },
  {
    "name": "kiwi",
    "color": "green",
    "price": 1.25
  },
  { 
    "name":"grapes",
    "color": "new",
    "price": 9.99
  }
]

# This is my JSON data so i want to display fruits which is above price 1 

# Output should be like below format:-
# Total we have 3 fruits with 1 price and fruits name is : Apple Kiwi gra

import json
mynewpath="fruits.json"
with open(mynewpath , 'w') as file:
    json.dump(mylist , file)

newlist =list()
with open(mynewpath , 'r') as file:
    data = json.load(file)
    print(type(data))
    print(data)
    
    for i in data:
        if i['price'] > 1:
            newlist.append(i['name'])
print(f"Total we have 3 fruits with 1 price and fruits name is  {newlist[0]} {newlist[1]} {newlist[2]}")    
    


###########################
import json

jsonfile=r"E:\Web Development\python learning\fruits.json"

with open(jsonfile,"r") as jf:
    my_dict= json.load(jf)
#print(my_dict)

mydata=[]
for i in my_dict:
    if i['price'] >=1:
        total_count=(len(i.keys()))
        mydata.append(i['name'])
print(mydata)
print(total_count)




# ------ File handling with csv  -------- 
mypath = 'E:\Web Development\python learning\servershealth.csv'
with open(mypath , 'r') as detailsfile:
    data = detailsfile.read()
    print(data)

#OR
with open(mypath,"r") as datafile:
    data=datafile.readlines()
    print(data)

#or
with open(mypath,"r") as datafile:
    data=datafile.readlines()

for i in data:
    print(i)

#or
with open(mypath,"r") as datafile:
    data=datafile.readlines()

for i in data:
    print(i.strip("\n"))

#OR
with open(mypath,"r") as datafile:
    data=datafile.readlines()

for i in data:
    print(i.strip("\n").split())


########
import csv
with open(mypath) as datafile:
    data=csv.reader(datafile)
    print(data)

with open(mypath) as datafile:
    data=csv.reader(datafile)
    for each in data:
        print(each)



#---csv file writing ------
import csv
filepath = 'E:\Web Development\python learning\servershealth.csv'
mylist=[12,'10.226.17.108','RHEL','d6:60:7b:6e:f6:9c','10 GB']
with open(filepath , 'a') as datafile:
    data_write = csv.writer(datafile)
    data_write.writerow(mylist)

#another exmple 
# import csv 
# mylist = [1, 'zia', 'kiani', 'kashmir']
# mylist2 = [2, 'ali', 'shekhani', 'pakistan']
# with open('myfile.csv' , 'a') as newfile:
#     data_write_file = csv.writer(newfile)
#     data_write_file.writerow(mylist)
#     data_write_file.writerow(mylist2)


#writerow vs writerows 

#writerow 
mylist=[1,'Abdeali','Dodiya','Bangalore']
mylist2=[2,'Ali','Dodia','Surat']
myfinal=[[1,'Abdeali','Dodiya','Bangalore'] ,[2,'Ali','Dodia','Surat']]
with open('myfile.csv' , 'w' , newline='') as file:
    data_write =  csv.writer(file)
    data_write.writerow(myfinal)
#output:-     not good
# "[1, 'Abdeali', 'Dodiya', 'Bangalore']","[2, 'Ali', 'Dodia', 'Surat']" 


#writerows
mylist=[1,'Abdeali','Dodiya','Bangalore']
mylist2=[2,'Ali','Dodia','Surat']
myfinal=[[1,'Abdeali','Dodiya','Bangalore'] ,[2,'Ali','Dodia','Surat']]
with open('myfile.csv' , 'w', newline='') as newfile:
    data_write_file =  csv.writer(newfile)
    data_write_file.writerows(myfinal)
#o/p:-
# 1,Abdeali,Dodiya,Bangalore
# 2,Ali,Dodia,Surat

with open('myfile.csv') as datafile:
    data=csv.reader(datafile)
    for each in data:
        print(each)

with open('myfile.csv') as datafile:
    data = csv.reader(datafile)
    data = list(data)
    print(data[0])

#to read the header of file 
with open('data.csv') as df:
    data =  csv.reader(df)
    header = next(data)
    print(header)

#to read csv file without header 
with open('data.csv') as df:
    data =  csv.reader(df)
    header = next(data)
    print(header)

    for i in data:
        print(i)

#i want to display only RHEL details
mypath =  "E:\Web Development\python learning\servershealth.csv"

mydata=[]
with open(mypath) as datafile:
    data=csv.reader(datafile)
    header=next(data)
    for each in data:
        if each[2] == 'RHEL':
            mydata.append(each)

print("#################")
print(mydata)


#now i want to store my data into csv file 
import csv
mypath =  "E:\Web Development\python learning\servershealth.csv"
mydata=[]

with open(mypath ) as df:
    data = csv.reader(df)
    for each in data:
        if each[2] == 'RHEL':
            mydata.append(each)
print(mydata)
with open('servershealth.csv', 'w' ,newline='') as df:
    data = csv.writer(df)
    data.writerow(header)
    data.writerows(mydata)

#Task time --------------
#I want to display serverlist whos less than 10 GB available memrory in mention CSV file.
print("################################")
import csv
mypath =  "E:\Web Development\python learning\servershealth.csv"
with open(mypath) as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        if row:
            try:
                val =  int(row[4].strip().split()[0])
                print()
                if val < 10:
                    print(row)
            except (IndexError , ValueError):
                continue
        
#Task -- #I want to disaply IP address only which belong to RHEL OS .
import csv
mypath =  "E:\Web Development\python learning\servershealth.csv"
with open(mypath ) as f:
    data = csv.reader(f)
    for d in data:
        if d:
            if d[2] == 'RHEL':
                print(d[1])
