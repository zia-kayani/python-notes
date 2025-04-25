print("hello world !!!")

# username=input("enter your name")
username="kayani"
print(username)

#to check length of a variable 
print(len(username)) 

str1="zia kayani"
stt=eval("44*44")  #eval evaluets the expression
print(stt)

astring="zia"
afloat=12.2
aint=44

print("your data types are :", type(astring), type(afloat), type(aint))
print("your values are : " + astring) 
#print("your values are : " + astring + " "+ afloat + " "+ aint) #error bcz no float or int concatinated
print("your values are : " , astring , " ", afloat , " ", aint) 
print(f"your vals are : {astring}  : {afloat} , {aint} ")

#we can also
print("your string is {} , your floating value is {} , your int value is".format(astring, afloat, aint))

print("your string is %s , your float val is %f and your int  val is %d" % (astring, afloat ,aint))

#escape sequences ------------------------------
#\n for new line 
print('zia \n kayani')

#slash 
mystr="\\zia\kayain"
print(mystr)

print("c:\\user\\nafi")

#\b   backspace
print("c:\\user\\zia\\Desktop\\lacture12\\devops\b6")

#\t   tab
print("\n \t\t zia")
print("\n\t kayani")

print("my name is 'zia' kayani")
print("my name is \"zia\" kayani")


#conditions ------------------------
# numb = int(input("Enter a number: "))
numb=12

if numb % 2 != 0:
    print("linkedin")  # Odd number
elif numb % 2 == 0 and numb in range(2, 5):
    print("not linkedin")
elif numb % 2 == 0 and numb in range(6, 20):
    print("linkedin ...")
elif numb > 20:
    print("not linkedin")

#string ----------------------------
mystirng="this is the testing string "
print(mystirng[-3])
print(mystirng[0:5])
print(mystirng[-1:-3])
print(mystirng[-1:-2])

s = "python"

print(s[-3:])     # 'hon' → last 3 letters
print(s[-4:-1])   # 'tho' → from -4 to -2
print(s[::-1])    # 'nohtyp' → full reverse


#string operations
mystr="i am devops and cloud engineer"
#uppercase
print(mystr.upper())

#lowercase
print(mystr.lower())

#casefold same as lowercase
print(mystr.casefold())

#capitalize
print(mystr.capitalize())

#title  -- will capitalize each first letter
print(mystr.title()) 

#swapcase   -- will convert to lower if upper or upper if lower
print(mystr.swapcase())

#checking bool value with "is"
print(mystr.isupper())

print(mystr.islower())

#to check digit
mynum=12
mynum=str(mynum)
print(mynum.isdigit())

#starts with and endswith
mystring="zia kayani"
print(mystring.startswith("zia"))
print(mystring.endswith("ki"))

#count
print(mystring.count("a"))

#index
print(mystring.index("a"))
# print("A") #will gen err not capital A

# print(mystirng.index("a",1)) #will show a at 1st position

#find
print(mystirng.find("k"))
print(mystirng.find("a",1))

#delete or modified
newstr ="zia"
del newstr
# print(newstr) #will cause error as no newstr is defined

# newstr[0] =12 #wil casue error string is immutable 