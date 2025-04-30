
# Types of error:-
# 1. Syntax Error
# 2. Logic Error 
# 3. Runtime error Or Exception handling 

# 1. Syntax Error :-
#    print("Abdeali Dodia"
#          ^
# SyntaxError: '(' was never closed

# You cant handle 


#2. Logic Error ---
a=100
b=20

if a>b:
    print("a is big")
else:
    print("b is  big")


#a=100
b=100

if a>b:
    print("a is big")
elif a==b:
    print(" Both a and b is same")
else:
    print("b is  big")



#3. Exception handling :-

# An Exception is error that happens during the execution of the program. Python generateds exception than could be handled. 
# You an define your own error its also called runtime error.


# a. NameError:-

# There are no error :-
x="ABD"
print("My value is ", x)

# O/p:
# My value is  ABD


# Error :-
x="ABD"
print("My value is ", x)
print("My value is ", y)

# O/p:-NameError: name 'y' is not defined


# try:
	#you can paste here your program
# except:
	#you can print your own error 

#Error handling or exception handling 
try:
    x = "ABD"
    print("My value is ", x)
    print("My value is ", y)
except:
    print("Something having issue")

#O/p:

# My value is  ABD
# Something having issue





try:
    #x = "ABD"
    y="Ali"
    print("My value is ", x)
    print("My value is ", y)
except Exception as e:
    print("Something having issue",e)

# O/p:-
# Something having issue name 'x' is not defined



# 2. Index Error :-
# We are checking Without Error :-
mylist=[2,7,8,9]
print(mylist)

# o/p:[2, 7, 8, 9]



# /mylist=[2,7,8,9]
print(mylist[4])

# O/p:
# IndexError: list index out of range


# With Execption handle:-
try:
    mylist=[2,7,8,9]
    print(mylist[4])
except Exception as e:
    print("Something issue : ",e)

# O/p:-
# Something issue :  list index out of range




# 3. Import Error:-  -----



# You can handle via execption handle:-
# import osss

# O/p:-ModuleNotFoundError: No module named 'osss'


try:
    import oss
    # os.system('dir')
except Exception as e:
    print('Something issue :' ,e)
# O/p:-
# Something issue : No module named 'oss'



# 4 zero diviion error ------

num1= int(input("enter the first numer"))
num2= int(input("enter the second number"))
result =  num1/num2
print(result)  #if num1 is 10 and num2 is 5 there willl no error
               #but if num1 is 10 and num2 is 0 , then there will be eorr
               # ZeroDivisionError: division by zero 

#to get rid of this error we use try : except 
try:
    num1= int(input("enter the first numer"))
    num2= int(input("enter the second number"))
    result =  num1/num2
    print(result)
except Exception as e:
    print("something went wrong", e) 


#5 - value error  ------
#if we pass ten as value in num1 that will give error in  above code

### Exception Handling  ####
# 1-   NameError -  y not found error
#2-    IndexError - index not found 
#3-    ModuleNotFoundError - No module named "osss"
#4-    ZeroDivisionError -  division by zero
#5-     ValueError -  Invalid literal for int() with base 10 : 'ten'

try:
    a=12, b=0
    print(a/b)
except:
    print("something went wrong")

try:  #nameerror
    #x="alian"
    y="zia"
    print("first value " ,x) 
    print("second value " ,y)
except NameError:
    print("issue in your variable name")

  
try: #index error
    x="alian"
    y="zia"
    mylist=[1,22,33,44]
    print("first value " ,x) 
    print("second value " ,y)
    print(mylist[4])
except NameError:
    print("issue in your variable name")
except IndexError:
    print("index out of range error ")


try: #module not found err
    import os
    x="alian"
    y="zia"
    mylist=[1,22,33,44]
    print("first value " ,x) 
    print("second value " ,y)
    print(mylist[4])
    print(os.system("uname"))
except NameError:
    print("issue in your variable name")
except IndexError:
    print("index out of range error ")
except ModuleNotFoundError:
    print('Module not found error , check module name')



try:  #0 division error
    import os
    x="alian"
    y="zia"
    mylist=[1,22,33,44]
    print("first value " ,x) 
    print("second value " ,y)
    print(mylist[4])
    print(os.system("uname"))
    a=1
    b=0
    print(a/b) #zero division error
except NameError:
    print("issue in your variable name")
except IndexError:
    print("index out of range error ")
except ModuleNotFoundError:
    print('Module not found error , check module name')
except ZeroDivisionError:
    print("zero is divided by value , error ")






try: #value error
    import os
    x="alian"
    y="zia"
    mylist=[1,22,33,44]
    print("first value " ,x) 
    print("second value " ,y)
    print(mylist[4])
    print(os.system("uname"))
    a=1
    b=0
    print(a/b) #zero division error
    print(b/x)
except NameError:
    print("issue in your variable name")
except IndexError:
    print("index out of range error ")
except ModuleNotFoundError:
    print('Module not found error , check module name')
except ZeroDivisionError:
    print("zero is divided by value , error ")
except ValueError:
    print("you can not divide integet with value like string")


#exception as and else 
try: #value error
    import os
    x="alian"
    y="zia"
    mylist=[1,22,33,44]
    print("first value " ,x) 
    print("second value " ,y)
    print(mylist[4])
    print(os.system("uname"))
    a=1
    b=0
    print(a/b) #zero division error
    print(b/x)
except NameError:
    print("issue in your variable name")
except IndexError:
    print("index out of range error ")
except ModuleNotFoundError:
    print('Module not found error , check module name')
except ZeroDivisionError:
    print("zero is divided by value , error ")
except ValueError:
    print("you can not divide integet with value like string")
except Exception as e:
    print("something went wrong in your code " ,e)
else:
    print("this is else statement")
finally:
    print("this will print definately ")

