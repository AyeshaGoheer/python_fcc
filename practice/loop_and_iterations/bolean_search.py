
# Search using a Bolean Variable

# TErminate the loop after meeting the condition
found = False
print("Before" , found)
for value in [9,25,12,15,3,19,3,3]:
    if value == 3:
        found = True
        break
    print(value , found)
print ("After" , found )



# Putting the TRue or False according to the condition
found = False
print("Before" , found)
for value in [9,25,12,15,3,19,3,3]:
    if value == 3:
        found = True
    else:
        found = False
    print(value , found)
print ("After" , found )

