x = "luminar Technologies"
searchKey = input("enter the key to be searches ")
pos = 0
for i in x:
    if i in searchKey:
        pos = 1
        break
    else:
        pos = 0
        continue

if pos == 0:
    print("not found")
else:
    print("found")
