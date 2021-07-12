def add(q, w, e, r, t):
    return q + w + e + r + t


def grade(tot):
    if tot > 90:
        print("A")
    elif 70 < tot <= 90:
        print("B")
    elif 50 < tot <= 70:
        print("C")
    elif 40 < tot <= 50:
        print("D")
    else:
        print("fail")


x = int(input("enter the mark"))
y = int(input("enter the mark"))
z = int(input("enter the mark"))
a = int(input("enter the mark"))
b = int(input("enter the mark"))
c = add(x, y, z, a, b)
print("mark is", c)
grade(c)
