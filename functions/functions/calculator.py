def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


a = int(input("enter the numer"))
b = int(input("enter the numer"))
print("1.Addition\n2.Substraction\n3.Division\n4.multiplication")
x = int(input("enter ur choice"))
if x == 1:
    print(sum(a, b))
elif x == 2:
    print(sub(a, b))
elif x == 3:
    print(div(a, b))
elif x == 4:
    print(mul(a, b))
else:
    print("wrong choice")
