#dictionary data struce ---------
# are aslo knows as assiciate arrays
# dictionary is the pair in unique keys 
# dictionary are oprimized to retrieve values if the key is known 
# are used to store the vlaues in key value format 
# dont allow duplicate values

mydict={"firstname":"zia", "lastname":"kayani"}
print(mydict)

print(mydict["firstname"])

mydict={"firstname":"zain", "lastname":"kiani"}
print(mydict)

print(type(mydict))

#accessing values by key
print(mydict["lastname"])

#INTERVIEW Q: how to handle exception while key not fuond 
print(mydict.get("firstname"))
print(mydict.get("Firstname")) #return none , as not match
print(mydict["firstname"])
# print(mydict["Firstname"])  #cause an error

#value assignment
mydict["firstname"]="zia ur rehman "
print(mydict["firstname"])

#copy 
mydict1=mydict
print(id(mydict))
print(id(mydict1)) #mydict and mydict1 will have same id bcz memeory allocation is same

mydict2=mydict1.copy()
print(id(mydict2))  #this will have diff id , 

#keys and values 
print(mydict.keys())
print(mydict.values())

#items
print(mydict.items())  #will shows keyvalue pairs in groups or items
dictitems= mydict.items()
print(dictitems)
print(type(dictitems))  #type will be dict-items
print(type(mydict))   #type will be dictionary 

#clear -- to clear or empty the dict
print(mydict2)
mydict2.clear()
print(mydict2)

#update
testdict={"name":"zia", "degree":"cs", "age":23}
testdict["age"]=24
testdict["degree"]="computer science"
print(testdict)
 

#pop method
dict1={"fname":"zia", "lname":"kiania", "age":22, "country":"kashmir"}
# dict1.pop()  #will cuase error, no key specified
print(dict1)

dict1.pop("fname")
print(dict1)

#popitem - will randomly pop 
# dict1.popitem("lname") #will cause error
print(dict1)

dict1.popitem()
print(dict1)

#del 
mydic={"fname":"zia", "lname":"kiania", "age":22, "country":"kashmir"}
# del mydic
# print(mydic) #will cause error 

del mydic["country"]
print(mydic)

#convert list to dictionary 
l1=[1,2,3,4]
l2=["one", "two", "three" , "four"]
convert_l=zip(l1, l2)
print(convert_l)

print(dict(convert_l)) #it made the dictinary form list

#FromKeys -- will also create dict from list but will assign vlaues 
              #and will take the keys from list 
myl=[1,2,4,5]
values="kiani"
dictionary=dict.fromkeys(myl ,values)
print(dictionary)

#set default
username={}
username.setdefault("first","zia")
print(username)
username.setdefault("secnd", "kayani")
print(username)

username.setdefault("abd", "abdiali")
print(username)

#sorted
print(sorted(username)) #will sort based on keys 

#how to check if key exisit in dictionary 
if "first" in username:
    print("data exist ")
else:
    print("data dont exitst")   

#nested dicionaries - --
myinfo= {
    1: {"fistname":"zia" , "lastname":"kayani"},
    2: {"fistname":"ali" , "lastname":"kammal"},
    3: {"fistname":"umar" , "lastname":"zian"},
    4: {"fistname":"ishtiaq" , "lastname":"kashif"}

} 
print(myinfo[1])
print(myinfo[4])
print(myinfo[1]["lastname"])

#max min sum keys values 
print(myinfo.keys())
print(myinfo.values())

print(max(myinfo))
print(max(myinfo.keys()))
# print(max(myinfo.values()))
print(sum(myinfo.keys()))

#nested dictionary with list
ls = {
    "servers1":["192.168.1.1" ,"192.168.1.2", "192.168.1.3"],
    "servers2": ["192.168.2.1", "192.168.2.2", "192.168.2.3"]
}

print(ls["servers1"][0])
print(ls["servers1"][1])
print(ls["servers2"][2])

##Tasks 
#input
myinfo = {
    "server1":{
        "ibm":{
            "datacenter":"pakistan",
            "env":{
                "PR":"192.168.1.1",
                "DR":"192.144.1.1"
            }
        }
    }
}
#ouput should be:  pakistan datacenter PR address is  PR":192.168.1.1
                # pakistan datacenter DR address is  PR":192.144.1.1

datacenter = myinfo["server1"]["ibm"]["datacenter"]
env = myinfo["server1"]["ibm"]["env"]

print(f"{datacenter} datacenter PR address is {env['PR']}")
print(f"{datacenter} datacenter DR address is {env['DR']}")
