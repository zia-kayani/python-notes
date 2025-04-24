#IF -ELSE -----------------------
age = 10
if age > 20:
    print('You are too old!')
    print('Why are you here?')
print('Why aren\'t you mowing a lawn or sorting papers?')

num=7
if num > 8:
    print("number is greater then 8")
print("number is less then 8 ")


#if else 
myage=22
if myage >= 25:
    print("you are eligible ")
else:
    print("you are not eligible ")

#elif
mynum=10
if mynum >=10:
    print("the number is greater then or equal to 10 ")
elif mynum >= 15:
    print("number is greater then or equal to 15  ")
elif mynum >= 20:
    print("age is greater then or equal to 20")
else:
    print("you entered wrong information")

#numbers and strings  ------------------------------
age =10
if age == 10:
    print("age is 10 ")
    print("hello there !!!")


myage='10'
if myage == 10:
    print("myage is converted from string to integer")

#to convert string to number or integer 
num="12"
num = int(num) #to convert number from string to integer 
if num == 12:
    print("number is 12")

#to convert number to string 
mynum = 12
newnum = str(mynum)

if newnum == "12":
    print("number is in string variable")
else:
    print("number is not in string")

#to convert decimal number to a number
mydec=10.12
mynewnum=int(mydec)
if mynewnum == 10: 
    print("number is right ")
else:
    print("number is in float ")


#for and while loop --------------------------------------
x=0
for x in range(0 , 19):
    print(x)

print(list(range(10,20)))  #using range and list togeather 

for x in range(0,5):
    print("salam %s" %x)

x = 0
y = 10

while x >= 10 and y <= 10:
    print("%s = x and %s = y" % (x, y))
    x += 1
    y -= 1

#functions ----------------------------------------
def myfunc(first , second):
    print(first , second)
myfunc("zia", "kayani")

first=10
second=12
def newfunc():
    return first * second
print(newfunc())

val=20
def hellfunc():
    val1=2
    val2=10
    return val+val2 * val
values =hellfunc()
print(values)
