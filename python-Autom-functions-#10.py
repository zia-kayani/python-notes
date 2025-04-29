#functions are used to do repeated tasks 
def first(abd):		#parameter
    print("my first function")
    print("my first function value is ",abd)

def second():
    ali=2
    print("my second function")
    print("my second function value is ", ali)
    first(ali)			#Arguments

second()

###recursive function ###
def add(a,b):
    c=a+b
    print(c)

def mycode():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    add(a,b)

mycode()

###############
#Variable lenght arguments :- *args  
server="IBM"
ip="192.168.1.1"
os="RHEL"

def mycode():
    print(f"Server is : {server}\n IP is {ip} \n OS is {os}")

mycode()



def mycode(server,ip,os):
    print(f"Server is : {server}\n IP is {ip} \n OS is {os}")
mycode("IBM","192.168.1.1","RHEL")


def mycode(*data):
    print(f"Server is : {data[0]}\n IP is {data[1]} \n OS is {data[2]}")

mycode("IBM","192.168.1.1","RHEL")


########################## **args

def mycode(**mydata):
    for k,v in mydata.items():
        print(k,v)
        
mydict={'server':'IBM','IP':'192.168.1.1','OS':'AIX'}
mycode(**mydict)

###Lambda Function ##############
# Lambda syntax:-
#lambda arguments: expression 


#Before :-
def mycode(ali,kazim):
    result=ali+kazim
    return result

print(mycode(20,10))


#After :-

result=lambda ali,kazim:ali+kazim
print(result(20,10))


result=lambda ali,kazim: ali if (ali >= kazim) else kazim
print(result(20,10))


#Def_function.py
import os
def mycode():
    print("This is my code function")
print(os.listdir(os.getcwd()))
print("My global print")




#test.py
#import Def_function
#Def_function.mycode()




#Def_function.py
import os
def mycode():
    print("This is my code function")

    

if (__name__=="__main__"):
	print(os.listdir(os.getcwd()))
print("My global print")


#test.py
#import Def_function
#Def_function.mycode()


