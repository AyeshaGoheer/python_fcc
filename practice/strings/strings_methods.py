
# Slicing in Srtrings
s = "hello world"
print(s[2:6])
print(s[ :6])
print(s[ 3: ])

# Strings Concatenation
a = "hello"
b = a + "there"
print(b)

# if need a space
a = "hello"
b = a + " "  + "there"
print(b)

# using in a logical operator
fruit = 'banana'
if "n" in fruit:
    print("found it")


# string library
greet = "hello Ayesha"
changed = greet.lower()
print(changed)

# we can call this method even on constants
print ("hi there". lower())

# finding the methods we can apply on strings

string = "hello world"
print(dir(string))

# searching/finding a string

fruit = "banana"
pos = fruit.find("na")
print(pos)

aa = fruit.find("z")
print(aa)


# search and replace in strings

greet = " hello ayesha"
replace = greet.replace("ayesha" , "inza")
print(replace)


# striping whitespaces in strings

greet = "   hello world   "
strip = greet.lstrip()
print(strip)

# rstrip
greet = "   hello world   "
strip = greet.rstrip()
print(strip)

# strip
greet = "   hello world   "
strip = greet.strip()
print(strip)



# parsing and extracting in strings

data = " ayesha.qayyum@phystech.edu.ru sat jan 2023"
pos1 = data.find("@")
print(pos1)
pos2 = data.find(" " , pos1)
print(pos2)
extracting = data[pos1+1 : pos2]
print(extracting)








