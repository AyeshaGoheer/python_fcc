
# append method
stuff = list()
stuff.append("book")
stuff.append(123)
print(stuff)


# using "in" operator with lists

list = [0,1,2,3,4,5]
print(4 in list)
print (15 in list)
print (20 not in list)


# lists are in order
names = ["mariam" , "inza" , "ayesha"]
names.sort()
print(names)
print(names[0])

# built in functions in lists
list = [20,40,12,34,10,2]
print(max(list))
print(min(list))
print(len(list))
print(sum(list))
print(sum(list)/len(list))



list = list()
while True:
    num = input ("enter a numnber: ")
    if num == "done": break
    value = float(num)
    list.append(value)
average = sum(list)/len(list)
print("average is :" , average)

