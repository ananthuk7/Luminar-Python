li = [1, 3, 2, 4, -1, -2, -3]
print(li.sort())
lth = len(li)

for i in range(0, lth - 2):
    for j in range(i + 1, lth - 1):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

print("min value", li[0])
print("max value", li[lth - 1])
