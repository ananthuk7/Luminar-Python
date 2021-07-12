def pyramid(n):
    k = n
    for i in range(0, n):
        for r in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0,n):
            print("*", end=" ")
        print('\r')


pyramid(5)