lst = [1, 2, 3, 4, 5, 6]
c = 0
ele = int(input("enter"))
for i in lst:
    if i == ele:
        c = 1
        break
if c == 1:
    print("found")
else:
    print('not found')


if ele in lst:
    print("found")
else:
    print("not found")
