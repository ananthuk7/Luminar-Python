x = int(input("enter the limit"))
first = 0
second = 1
print(first)
print(second)
for i in range(2, x):
    third = first + second
    first = second
    second = third
    print(third)
