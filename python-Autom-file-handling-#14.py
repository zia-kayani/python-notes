#file handling  --------------

#first we open file, then read, then close the file 
#file must be closed if that being open 

file =  open("zia.txt")
data= file.read()
print(data)
file.close()

#OR we can also do like this 
with open("zia.txt") as file:
    data =  file.read()
    print(data)
    file.close()

#we can read a file line by line 
with open('zia.txt') as file:
    data =  file.readlines()
    print(data)
    file.close()

#with open keywords open the file and runs the file and close that automatically
#we can split words 
with open('zia.txt') as file:
    data = file.readlines()
    print(data)
    for i in data:
        word =  i.split()
        print(word)

#we can also give absolute path of the file like
with open('E:\Web Development\python learning\zia.txt ') as file:
    data =  file.readlines()
    print("####")
    print(data)




#file writing  ---------------------------------
#we can read the file in these ways 
file  = open('zia.txt')
data =  file.read()
print(data)

with open('zia.txt') as file:
    print(file.read())

with open('zia.txt' , mode='r') as file:
    print(file.read())

with open('zia.txt' , 'r') as file:
    print(file.read())

#ways to write the file 
#write will overwrite the file 
# with open('zia.txt') as file:
#     file.write('hello from zia kayani') #will cause error : 
#                                         #io.UnsupportedOperation: not writable

with open('zia.txt' , mode='w') as file:
    file.write('zia kayani is from neelum valley kashmir')

#OR
with open('zia.txt', 'w') as file:
    file.write('hello from jammmu and kashmir')

#multiline writing 
with open('zia.txt', 'w') as file:
    file.write("hello there \n")
    file.write("i am zia \n")
    file.write("from jammu kashmir \n")



#Append in file 
#append is use for append your data as well as creating file if file is not present.
with open('zia.txt' , 'w') as file:
    file.write("zia kayani kashmiri")

with open('zia.txt', 'a') as file:
    file.write('\n computer science engineer')


mylist = ['zia', 'kayani', 'kashmiri', 'computer', 'science']
with open('zia.txt' ,'w') as file:
    for i in mylist:
        file.write(i+" ")

for i in range(11):
    with open("zia.txt",'a') as file:
        file.write(f"Line : {i}\n")

#read data with binary mode :-
#if we have binary or any other execuatble file we can 
#read date from that
# with open("zia.bin","rb") as file:
#     data=file.read()
#     print(data)


