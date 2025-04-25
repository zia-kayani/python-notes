#moduels in python ----------------------------
import math
print(math.sqrt(81))

#classes and objects -----------------------------------------------------------
class things:
    pass
class inanimate(things):
    pass
class animate(things):
    pass
class animals(animate):
    pass
class mammels(animals):
    pass
class girrafe(mammels):
    pass

myobj= animals()  #object 


#functions inside the classes 
class myclass:
    def myfun():
        print("hello from myclass fun !!!")
def normal_func():
    print("hello from normal function !!!!")
normal_func()



#build in functions in python  ------------------------------------------------
#abs , dir, bool etc

#abs 
print(abs(22.2))
print(abs(-20))
print(abs(-20.30))

#bool
test=[]
print(bool(test))

test=" "
print(bool(test))

test=[0]
print(bool(test))

test=0.0
print(bool(test))

test=None #none is used to keep the vairable empty intentially , 
print(bool(test))

test=True
print(bool(test))

test = "zia kay7ani"
print(bool(test))

#dir 
myl=[1,2,3,4]
print(dir(myl))

print("return values from empty dir", dir())

print(dir("hello"))  #will return all string methods
import math
print(dir(math))  #will return all the attributes or methods of math func

#strings ---------------------------------------
#we can write strings in three ways 
mystr="hello this is zia kayani "
mystr1='hello from zia'
mystr2='''
    hello there from zia 
 '''
myste3=" hello from 'zia' kayani "

#strings are immutable , we can not change values of string
#string methods
mystring ="zia kayani !!!"
mystring.upper()
print(mystring)

mystring.lower()
#converting string to number
mystr = "213"
print(int(mystr))

#string slicing
mystring="this is zia kayani from lahore"
print(mystring[0])
print(mystring[0:10])
print(mystring[0:-3])  #to reversse -3 characters

#string substitution formatting
varr="cookies"
my_message="i like %s " %varr
print(my_message) 

varr1="chocolates"
mystr="i am %s developer"  % "python"
print(mystr)

print("i like %s and i am %s" % (varr1 , "Devops Engineer"))

#integer subs in string
my_sting = "%i + %i = %i" % (1,2,3)
print(my_sting)

#float substition in string 
myfl= "%f" % (12.11)
print(myfl)

myfl2="%.2f" % (12.8888)
print(myfl2)

#dictionary substition method in string 
mydic="my name is %(name)s and i am from %(country)s" % {"name":"zia kayani", "country":"kashmir"}
print(mydic)

#another substition 
myvals="x values is = %(x)i and y values is %(y)i " % {"x":1, "y":2}
print(myvals)

#another method for substitution 
mv="python is as simple as {0}, {1} , {2}".format("a", "b","c")
print(mv)

myvals={"x":0, "y":1}
print("two values are x={x} and y={y}".format(**myvals))