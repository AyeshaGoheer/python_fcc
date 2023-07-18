
# counting in loop

a = 0
print("Before", a)
for thing in [10,23,45,67,89]:
    a = a + 1
    print(a, thing)
print("After", a)


a = 0
print("Before", a)
for thing in [10,23,45,67,89]:
    a = a + thing
    print(a, thing)
print("After", a)

