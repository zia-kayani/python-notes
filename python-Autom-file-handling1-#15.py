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