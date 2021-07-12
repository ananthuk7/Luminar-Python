x = int(input("enter the range"))
num=1
for i in range(0, x):

    for j in range(0, i):
        print(num, end=" ")
        num += 1
    print('\n')
