def fact(num):
    factorial = 1
    for i in range(2, num+1):
        factorial = factorial * i
    print(factorial)


num1 = int(input("enter the number1"))
fact(num1)
