set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 70, 65, 43, 56, 23, 14, 63, 78}
odd = set()
even = set()
for i in set1:
    if i % 2 == 0:
        odd.add(i)
    else:
        even.add(i)

print("odd sets are", odd)
print("even sets are", even)
