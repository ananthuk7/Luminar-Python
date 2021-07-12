# exception handling connect unexpected errors
# try- exceptional code
# expect solving code
# finally anything


num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
try:
    print(num1 / num2)
except Exception as e:

    print("error occurred", e)
finally:
    print("inside finally")
