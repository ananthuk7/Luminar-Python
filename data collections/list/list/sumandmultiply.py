
lst = [1, 8, 9, 7, 6, 5, 544, 3, 2, 44]
add, mul = 0, 1

for i in lst:
    add += i
    mul *= i

print("sum is", add)
print("multiplied value is", mul)
print(sum(lst))

