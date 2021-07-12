def trapiz(n, ran):
    k = n-ran
    r = ran
    for i in range(ran, n):
        for r in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print('\r')


size = int(input("enter the limit"))
hgt = int(input("enter the height of trapi"))
if hgt<size:
    trapiz(size, hgt)
else:
    print("height is greater than or equal your limit")
