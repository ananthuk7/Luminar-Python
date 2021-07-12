a = []
n = int(input("enter the limit"))


def left(frond):
    a.append(frond)


def right():
    a.pop(0)


def display():
    print(a)


print("choose your operation to be perform")
while 1:
    print("1. ENQUEUE 2. DEQUEUE 3. Display 4.exit")
    ch = int(input())
    if ch == 1:
        if len(a) == n:
            print("queue is full")
            print("please perform DEQUEUE operation")
        else:
            ele = int(input("enter the element"))
            left(ele)
    elif ch == 2:
        if len(a) == 0:
            print("queue is empty")
            print("please perform ENQUEUE operation")
        else:
            right()
    elif ch == 3:
        display()
    else:
        break

# rear=0
# front=0
