x = 10  # global


def printab():
    global y
    y = 1
    x = 5  # local
    print(x)


printab()
print(x)
print(y)
