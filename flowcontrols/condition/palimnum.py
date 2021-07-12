def rev(num):
    rev1 = 0
    while num > 0:
        r = num % 10

        rev1 = (rev1*10)+r

        num = int(num / 10)
    return rev1


x = int(input("enter the number"))
y = rev(x)
print(y)
if x == y:
    print("palindrome")
else:
    print("not palindrome")
