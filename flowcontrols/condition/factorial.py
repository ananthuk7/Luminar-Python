x = int(input("enter the limit "))
if x > 0:
    if x == 0:
        print("0")
    else:
        fac = 1
        for i in range(1, x + 1):
            fac = fac * i
        print(fac)
