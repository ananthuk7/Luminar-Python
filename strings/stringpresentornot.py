x = "luminar Technologies"
searchKey = input("enter the key to be searches ")
pos = 0
for i in x:
    if i == searchKey:
        pos = 1

    else:
        pos = 0

if pos == 0:
    print("not found")
else:
    print("found")
