a = [1, 2, 3, 4, 5, 6, 7]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)


# new method
# list comprehence

b = [i * 5 for i in a if i % 2 == 0]
print(b)
