# print("hello world !!")

# print(12+12)

# print(2+2*(4+5))

# variables
ali=12
umar=12
usman=12
abubakar=12
result=ali+umar + usman +  abubakar
print(result)


#write in many lines 
abubakr = '''first
Righteous
caliph!!'''
print(abubakr)

#quotation inside the quotation
print(' hello "zia"')
silly_string = '''He said, "Aren't can't shouldn't wouldn't."'''
print (silly_string)

#escape sequences ------------------------
#single quote string
single_quote_str='He said , " me ,umar\'s ali\'s result is shown "'
print (single_quote_str)
#double quote string 
double_quote_str=" he said \" me and ali will go \""
print(double_quote_str)


#string substitutions
my_score=1000
message='i scored %s points'
print(message % my_score)

nums="%s this is the first number &  %s this is the second number"
print(nums % (44,55) )

firstname='zia'
secondname='kayani'
message="%s= frist name && %s= second name "
print(message % (firstname , secondname))


#string multiplications -------------------------
print( '*' * 10)
spaces=' ' * 20
print('%s after 10 spaces' % spaces)

print(50 * 'zia')


#list and strings --------------------
mystr = "hello this is zia kayani "
print(mystr)

mylist=["hello this is zia kiani"]
print(mylist[0])

my2ndlist=["zia","kayani","kashmiri"]
print(my2ndlist[2])
print(my2ndlist[0:3])

my3rdlist=["zia",1,"kayani",2]
print(my3rdlist)
print(my3rdlist[1])

myls1=["hello", "zia"] 
myls2=["hi ","kayani"]
lswls=[myls1, myls2] #list within alist 
print(lswls)

#adding items to a list 
mylist = ["zia","kayani",11,22,"kashmir"]
mylist.append("janwai")
print(mylist)

#deleting from the list 
del mylist[5]
print(mylist)

#concatinate lists
l1=[1,2,3]
l2=[4,5,6]
lsum=l1+l2
print(lsum)

#multiplying lists 
print(l1 *3) #this will repeat the list to number which is multiplying

print(l1 / 3) #division will give an error 
################################################################

#TUPLE ----------------------------
mytuple=(1,2,3,4)
print(mytuple[1])

mytuple[0]=0  #we can not chnage hte values in tuple 
print(mytuple)

#Map ----------------------------------
#maps are just dictionaeris in which we can store our data in the key value pairs 
mymap=["zia,devops", "nouman, full stack", "ali, frontend"]
print(mymap)

#another way to write maps 
staff={
    "Ali":"software engineer",
    "zia":"Devops Engineer",
    "usman":"software engineer",
    "zain":"frontend engineer"
}

print(staff["zia"])

#to delete the last value from map
del staff["zain"]
print(staff)

#replacing a value 
staff["usman"] = "QA engineer"
print(staff)

staff1={
    "test":"testing"
}

lll= staff+staff1   #we cant joint two maps 
print(lll)