set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 70, 65, 43, 56, 23, 14, 63, 78}
set2 = {1, 2, 3, 4}
common = set()
for i in set2:
    if i in set1:

        common.add(i)
print(set1)
print(set2)
print("common elements are",common)