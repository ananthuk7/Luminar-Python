def rectangle(n):
    for i in range(0, int(n / 2)):

        for j in range(0, n):
            print("*", end=" ")
        print('\r')


rectangle(10)

h = int(input("enter the height"))
w = int(input("enter the width"))
for i in range(0,h):
    for j in range(0,w):
        print("*", end=" ")
    print('\r')
