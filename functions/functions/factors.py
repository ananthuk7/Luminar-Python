def prime(n):
    flag = 0
    for i in range(2, n):
        if n % i != 0:
            flag = 0
        else:
            flag = 1
            break

    return flag


num = int(input("enter the number"))
if num > 0:
    v = prime(num)

    if v == 1:
        print(" not prime")
    else:
        print(" prime")

    # simple method
    # print(num)
    # for i in range(2, num):
    #     if num % i == 0:
    #         print("not prime")
    #         break
    #     else:
    #         print("prime")
