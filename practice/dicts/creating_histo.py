

# when we see a new name

# when encounter new name want to add entery in dict
counts = dict()
names = ["ayesha" , "inzas" , "mariam" , "abood" , "rehan", "ayesha"]
for name in names:
    if name in counts:
        counts [name] = counts [name] + 1
    else:
        counts[name] = 1
print(counts)