x = int(input("enter the number"))
y = int(input("enter the number"))
z = int(input("enter the number"))

if x > y and x > z:
    print("x is greater", x)

elif y > x and y > z:
    print("y is greater", y)
elif z > x and z > y:
    print("z is greater", z)
else:
    print("equal")
