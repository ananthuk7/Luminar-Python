def pyramid(n):
    k = 0
    for i in range(n,-1,-1):
        for r in range(0, k):
            print(end=" ")
        k = k + 1
        for j in range(0, n):
            print("*", end=" ")
        print('\r')


pyramid(10)