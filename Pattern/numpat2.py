x = int(input("enter the range"))

for i in range(0, x):
    num = 1
    for j in range(0, i):
        print(num, end=" ")
        num += 1
    print('\n')

for i in range(0, x):

    for j in range(0, i):
        print(j+1, end=" ")

    print('\n')