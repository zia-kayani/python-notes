#Reguler expressions are used to find the specific string from your program 
#its a sequence of characters 

#reguler expressoins:-
# 1 match()
# 2 search()
# 3 findall()
# 4 sub()
# 5 subn()
# 6 split()
# 7 compile()


#------  findall() ---------
#syntext:
# re.findall(pattern , text)

import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we" \
" will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = 'python'
print(re.findall(pattern, myword))


import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = 'python2'
print(re.findall(pattern, myword))

import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = 'Python'
print(re.findall(pattern, myword))

#we can also find python2 lik this 
import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = "python[2]"
print(re.findall(pattern, myword))

#we can find also like this for example 
#we have to find  python2 pr python3 etc 
import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = "python[234]"
print(re.findall(pattern, myword))

#to find simple python we will put quotes 
import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern = "python[' '23]"
print(re.findall(pattern, myword))

#we cal alos use like this 

import re
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="python2|python3|python|Python"
print(re.findall(pattern,myword))

####################
#\w  it will include a-z  A-Z  0-9
pattern = "\w"
print(re.findall(pattern, myword))

#This will print all words or sequences of 7 consecutive word characters
pattern = "\w\w\w\w\w\w\w"
print(re.findall(pattern, myword))

#opposite of \w means will match spaces not character
pattern = "\W"
print(re.findall(pattern, myword))

#\S will match characters not spaces . works like \w
pattern = "\S"
print(re.findall(pattern, myword))

#\d matches digit from  0-9
pattern = "\d"
print(re.findall(pattern, myword))

# '.'   matches single character
pattern = "."
print(re.findall(pattern, myword))

# .......  matches 7 character word
pattern = "......."
print(re.findall(pattern, myword))

#\.  find only dot in the string
pattern = "\."
print(re.findall(pattern, myword))

#\.\w\w\w  find three character string after dot . like .com
myword="hello there from zia@gmail.com"
pattern="\.\w\w\w"
print(re.findall(pattern ,  myword))

#\@\w\w\w\w\w\\.\w\w\w   find @ and after it 5 characters and then dot & after it three charcter
#like @gmail.com
pattern="\@\w\w\w\w\w\\.\w\w\w"
print(re.findall(pattern , myword))

#? optional characher
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="python?"
print(re.findall(pattern , myword))

# $   find word at the end of string 
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we" \
" will learn two version such python2 and python3, We will learn " \
"Python selenium in this course"
pattern="python$"
print(re.findall(pattern , myword))

#\b matches at the start and end of string - matches the whole word
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will " \
"learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="\bcourse\b"
print(re.findall(pattern , myword))

#\\b will match all courses
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will " \
"learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="\\bcourse"
print(re.findall(pattern , myword))


#\b will match all courses
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will " \
"learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="\\bcourse\\b"
print(re.findall(pattern , myword))

# Matches  only if it's inside another word (e.g.,course from  'thiscoursewe')
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will " \
"learn two version such python2 and python3, We will learn Python selenium in this course"
pattern="\\Bcourse\\B"
print(re.findall(pattern , myword))

# \\t maches the tab 

pattern = "\\t"
print(pattern , myword)

# \\t maches the tab 

pattern = "\\n"
print(pattern , myword)


#######################################
#will find the exact word  \\b___\\b
pattern = r"\\bpython\\b"
print(re.findall(pattern, myword))

#match the n no of repeatitions
myword="Abdeali Dodiya from bangalore , We are learning python and in this course we will " \
"learn two version such python2 and python3, We will learn Python selenium in this coursesss"
pattern=r"\bcoursesss\b"
print(re.findall(pattern , myword))

import re
myword="Abd$%*eal2@1i Dodiya from bangalore , Python is very good language abdealipython@gmail.com We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this coursesss"
pattern=r"\bcourses{3}\b"
print(re.findall(pattern,myword))


pattern=r"\bpython\b"
print(re.findall(pattern,myword))

pattern=r"\bpython\d\b"
print(re.findall(pattern,myword))

##
import re
mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11"
print(mytext)

#to find the ip 
pattern="\d\d\d.\d\d\d.\d.\d\d"
print(re.findall(pattern ,  mytext))

pattern="\d\d\d.\d\d\d.\d.\d"
print(re.findall(pattern ,  mytext))

# 1 time or two time or three time 
pattern = "\d{3}.\d{3}.\d{1}.\d{1}"
print(re.findall(pattern, mytext))

pattern = "\d{3}.\d{3}.\d{1}.\d{2}"
print(re.findall(pattern, mytext))

mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255"
pattern=r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
print(re.findall(pattern,mytext))

import re
mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(re.findall(pattern,mytext))

#{1,} one or more times 
pattern=r"\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}"
print(re.findall(pattern,mytext))

# + --> same as {1,} one or more times 
import re
pattern=r"\d+\.\d+\.\d+\.\d+"
print(re.findall(pattern,mytext))

#will also show invlid ip addresses
import re
mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address" \
" is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address " \
"192.168.1234.12345 \n my invalid address is 0..12.34"
pattern=r"\d+\.\d+\.\d+\.\d+"
print(re.findall(pattern,mytext))

# * ---> 0 or more times 
pattern=r"\d*\.\d*\.\d*\.\d*"
print(re.findall(pattern,mytext))

# ? --> 0 times or none times 
pattern=r"\d?\.\d?\.\d?\.\d?"
print(re.findall(pattern,mytext))

###################
import re
myword="Abd$%*eal2@1i Dodiya from bangalore , Python is very good language" \
" abdealipython@gmail.com We are learning python and in this course we will " \
"learn two version such Python2 and python3, We will learn Python selenium in this coursesss"
pattern=r"\bpython\d\b"
print(re.findall(pattern,myword))

#now this will ignore case insansetiveness
pattern=r"\bPython\d\b"
print(re.findall(pattern,myword,re.I))
#OR we can use this syntext
# print(re.findall(pattern,myword,re.IGNORECASE))

############
re.M

import re
mytext="""My jboss server ip address is 192.168.1.8 
My Docker server ip address is 192.168.1.11 
My broadcast addres is 255.255.255.255 
My invalid address 192.168.1234.12345 
my invalid address is 0..1.3
"""
pattern=r"^My" #will match My at start of string but on one line
print(re.findall(pattern,mytext))

pattern=r"^My"
print(re.findall(pattern,mytext,re.M)) #will match My at start of string but from many lines
#OR we can use 
pattern=r"^My"
# print(re.findall(pattern,mytext,re.MULTILINE))

#If you want to use multiline and ignorecase same pattern then you can use | sigh in your findall arguments 
pattern=r"^My"
print(re.findall(pattern,mytext,re.M|re.I))

###############
print(len(re.findall(pattern,mytext)))

#finiter  -- returns the iterable 
import re
mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(re.findall(pattern,mytext))
print(re.finditer(pattern,mytext))

print("#########")
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myiter=(re.finditer(pattern,mytext))
print(myiter)
for i in myiter:
    print(i)


print(type(myiter))  #callable iterator 

#to show only the matched value from iterator
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myiter = (re.finditer(pattern , mytext))
for i in myiter:
    print("My matching string is ", i.group())



# ----------- re.compile() method ---
#this is used to compile the reguler expression for reuse
#like we used to do 
import re
mytext="We are learning python automation course, In devops course python is very important"
pattern = r"\bpython\b"
print(type(pattern))  #type will be kind of str
print(re.findall(pattern ,  mytext))

#but we can use
pattern = re.compile("python")
print(type(pattern))   #type willl be re.pattern
print(re.findall(pattern ,mytext))


# ---- search()  methodd ----------------
#alternative to findall method , but give first matched result
#in the form of object

import re
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.findall(pattern,mytext))
print(myfind)

#now with search we can do the same 
import re
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.search(pattern,mytext))
print(myfind)


print("we found from string" , myfind)
print("we found from string" , myfind.group())
print("starting index " , myfind.start())
print("ending index ", myfind.end())
print("search length is ", myfind.end() - myfind.start() )

# pattern=r"ABD\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# myfind=(re.search(pattern,mytext))
# print('We are found some string from pattern',myfind)
# print('We are found some string from pattern', myfind.group())  #will cause an error

###################
#You can find character string more than 7 to 8 character 
import re
abd="Abdeali"
pattern=r".{7,}"
print(re.search(pattern,abd))


#You can check whether your string is upper case or not 
import re
abd="ABDEALI"
pattern=r"[A-Z]"
print(re.search(pattern,abd))