# stack
# stack operations

# 1 push ... add elements
# 2 pop ... pop elements
# last in first out


n = int(input("enter the limit"))
a = []
while True:
    print("enter the operation want to perform")
    print("1. push 2. pop 3. Display")
    ch = int(input())
    if ch == 1:
        if len(a) == n:
            print("stack full")
        else:
            c = int(input("enter the element to push"))
            a.append(c)
            cont = int(input("Do you want to continue press one"))
            if cont != 1:
                print(a)
                break
            else:
                continue
    elif ch == 2:
        if len(a) == 0:
            print("stack is empty")
            continue
        else:
            a.pop()
            cont = int(input("Do you want to continue press one"))
            if cont != 1:
                print(a)
                break
            else:
                continue
    elif ch == 3:
        print(a)
