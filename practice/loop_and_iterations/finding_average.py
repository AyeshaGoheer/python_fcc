
#Finding Average in the loop

count = 0
sum = 0
print ("Before", count, sum)
for value in [10,23,45,67,89]:
    count = count + 1
    sum = sum + value
    print (count , sum )
print ("After", count , sum , sum/count)


