

# checking if a "key" exists or not is so common that dict object has e method "get" to check it avoiding more lines of code
# dict = {'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}
# existence = dict.get(name , 0)


counts = dict()
names = ["ayesha" , "inzas" , "mariam" , "abood" , "rehan", "ayesha"]
for name in names:
 # Use get() to check if the name exists in the counts dictionary.
 # If it exists, get the current count. If not, set the count to 0.
        count = counts.get(name , 0) 
        counts[name] = count + 1

print(counts)

