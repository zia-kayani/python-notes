#lists
mylist=[]
mylist =list()

l1=[1,2,4,"kiani"]
l2=["zia", 12]
combo = [l1,l2]
print(combo)

l3=[12,234,545,33]
combo.extend(l3)
print(combo)

#tuple
mytpl=(1,2,3,4)
print(mytpl)

print(mytpl[0:2])

#dictionary 
mydic = {}
#or
mydic = dict()
mydic={"name":"zia", "caste":"kayani"}
print(mydic)

print("name" in mydic)

print(mydic.keys())

#IF condition with and or not  -----------------------
val=11
if  val < 20:
    print("values is less then 20")
elif val > 10 and val < 20:
    print("value is greater then 1o and less then 20")
elif val > 10 or val < 20:
        print("value is greater then 1o or less then 20")
else:
     print("vlaue is not less then 20")

#not 
mylist=[12,23,5,33,11]
if val not in mylist:
     print("value is not in the list my list ")
else:
     print("value is in my list ")


my_list = [1, 2, 3, 4]
x = 10
z = 11
if x not in my_list and z != 10:
    print("This is True!")


#loops ------------------------------
#For loop
print(range(10))
print(range(5,10))

for numbers in range(5):
    print(numbers)

for val in [0,1,2,3,4]:
    print(val)

print("###########################3")

my_dic = {1:"Zia", 2:"kashif", 3:"asad"}
for keys in my_dic:
    print(keys)


my_dic = {6:"Zia", 2:"kashif", 5:"asad"}
all_keys = my_dic.keys()
sorted(all_keys)
for keys in all_keys:
    print(keys)

i= 0
while i< 10:
    print(i)
    if i==5:
        print("i is = 5")
        break
    i+=1


#comprehensions -----------------------------------
#are a way to write more consize code like 
#list comprehension
mylist=[]
for x in range(5):
    mylist.append(x**2)
#instead we can do this shortly
mylist=[ x**2 for x in range(5)]

print(mylist)

myls =list()
myls = [x**2 for x in range(5) if x % 2 == 0]
print(myls)


myls = ['0','1', '2']
myls2=[int(num) for num in myls ]
print(myls2)

#nested 
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)

#dicotnary  comprehenion 
squares = {x : x**2 for x in range(5)}
print(squares)

original={'a':1, 'b':2, 'c':3} #swapped dictionary example 
swapped = { v : k for k , v in original.items()}
print(swapped)

dic2={'a':1, 'b':12, 'c':11}
evendic= {k:v for k , v in dic2.items() if v % 2==0}
print(evendic)

#set comprehenion   set dont repeat values
my_set = [1,2,2,3,4,5,5,6]
sett =set(my_set)
print(sett)

ns =  {x for x in my_set}
print(ns)

#exception handling in python  ------------------------
my_dict = {"a":1, "b":2, "c":3}
try:
    print(my_dict["d"])
except:
    print("some error occuered")

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")

#or we can use ()
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")


#importing from the moudle  --------------------------------------
from math import sqrt
print(sqrt(81))


#functions -------------------
def myfun ():
    pass #pass means do nothing 

#classes ---------------------
class animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        print(self.name)

obj1 =  animal("cow")
obj1.speak()


