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
    



