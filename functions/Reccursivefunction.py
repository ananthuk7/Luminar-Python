def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


x = int(input("enter the number"))
for i in range(0,x):
    print(fibo(i))