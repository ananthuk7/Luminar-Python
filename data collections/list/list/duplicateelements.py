a = [1, 2, 2, 3, 3, 66, 66, 1, 1]

dup = a[0]
d = []
for i in range(len(a) - 1):
    if dup in a[i + 1:]:
        if dup in d:
            continue
        else:
            d.append(dup)
    dup = a[i + 1]
print(d)

b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)
