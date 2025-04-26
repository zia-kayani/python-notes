#LIST data structure operations  ----------------------
abd=(1,2,53,6,32,8,5)
print(type(abd))

abd= list(abd)
print(type(abd))

print(list(range(1,10))) #upto 10
print(list(range(1,10+1)))
print(list(range(10,21)))

#covert to set
abd=[1,2,4,7,0,8]
print(set(abd))
print(list(set(abd)))

#count to count specific values in list
print(abd.count(2))

#min , max adn sum values in list
print(min(abd))
print(max(abd))
print(sum(abd))

#copy in string 
abd=[5,2,6,3,9]
abd1=abd.copy()
print(abd1)

abd2=abd1
print(abd2)

print(id(abd))
print(id(abd1))
print(id(abd2))


#concatinate
abdcon=[abd1 , abd2] #this will append two lists in one list
print(abdcon)

abdnew=[12,234,535]
print(abd+abdnew) #this will concatinate and join two list in one

#append method
print(abd)
abd.append(10)  #will add new item in list at end
print(abd)

abd.append("zia")
print(abd)

#extend method -- this will extend previous list with new list items
abd=[1,2,3]
abd1=[4,5,6]
abd.append(abd1)
print(abd)

abd=[1,2,3]
abd1=[4,5,6]
abd.extend(abd1)
print(abd) #this will  make one list 

#reverse method 
abd=[1,2,5,3]
abd.reverse()
print(abd)

#second method for reverse
abd=[12,3,5,7]
print(abd[::-1])

#sort method of list
abd=[1,2,3,8,4,7]
abd.sort() #ASC order sort
print(abd) 

abd.sort(reverse=True) #soert in Desc
print(abd)

print(dir(abd))

#TASK 
# input = ["zia", "kayani", "kashmiri"]
# output = zia kayani kashmir 
mylist=["zia", "kayani", "kashmiri"]
print( " ".join(mylist))

