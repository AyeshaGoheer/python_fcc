# iterations

smallest_so_far = float('inf')
print("Before", smallest_so_far)

for num in [9, 25, 12, 15, 3, 30, 3, 3]:
    if num < smallest_so_far:
        smallest_so_far = num
    print(smallest_so_far, num)

print("After", smallest_so_far)