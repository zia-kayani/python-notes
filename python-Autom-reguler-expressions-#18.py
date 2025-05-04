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
