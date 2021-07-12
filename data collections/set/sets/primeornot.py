set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 70, 65, 43, 56, 23, 14, 63, 78}
prime = set()
notPrime = set()
for i in set1:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                notPrime.add(i)
                break
        else:
            prime.add(i)

print(prime)
print(notPrime)
