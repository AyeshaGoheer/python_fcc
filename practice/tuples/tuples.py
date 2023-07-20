


# tuples are like lists
tuple = ("ayesha" , "inza" , "mariam")
print(tuple[1])
tuple1 = (1,2,3,4)
print(tuple1)
print(max(tuple1))


# tuples are "immutable" , only difference between lists and tuples
# tuple[2] = "abood"
# print(tuple)


# methods we can apply on tuples
# print(dir(tuple))

"""
 tuples and assignments
 we can even assign tuples on left-hand-side
 we can even omit prantheses
"""
(x,y) = ("ayesha" , "mariam")
print(y)

# tuples and items
# we can use "items" method
# "items" in dict returns the key value paits in the form of tuples 

dict = {"money" : 34 , "day" : 2 , "age" : 28 }
print(dict.items())


# tuples are compareable
x = (0,1,2) < (4,8,10)
print(x)

# sorting lists of tuples, using "items" method and "sorted" funtion
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
print(dict.items())
print(sorted(dict.items()))

# sort by values instead of key
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
list = list()
sort = sorted(dict.items())
for k , v in sort:
    list.append((v , k))
print(list)

# using "reverse" argument in sorted
list1 = sorted(list , reverse=True)
print(list1)







