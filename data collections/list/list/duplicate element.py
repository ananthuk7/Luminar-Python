# a = [1, 0, 7, 5, 9, 2, 3, 5, 7, 2, 0, 1, 10]
# b = []
# [b.append(i) for i in a if i in b]
# print(b)

# list1 = [3, 5, 7, 9, 0, 8, 55, 34, 23, 76, 4, 65, 12, 89, 56, 76, 34, 289, 49, 12, 63, 976]
# list1.sort()
# length=len(list1)-2
# print(list1[length])


# a = [1, 2, 3, 45, 6, 7, 33, 11, 77, 9, 0, 5]
# b = [3, 77, 0, 5, 33, 6, 22, 5, 90, 32, 56, 78, 98, 54, 67, 11, 34, 88]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)


# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def mul(a, b):
#     return a * b
#
#
# def div(a, b):
#     return a / b
#
#
# def floor(a, b):
#     return a // b
#
#
# while True:
#     x = int(input("enter the 1st number"))
#     y = int(input("enter the 2nd number"))
#     print("1.Addition\n 2.subtraction\n 3.multiplication \n4.division  \n 5.floor division\n")
#     ch = int(input("enter your choice"))
#     if ch == 1:
#         print("sum is ", add(x, y))
#
#     elif ch == 2:
#         print("sub is ", sub(x, y))
#     elif ch == 3:
#         print("mul is ", mul(x, y))
#     elif ch == 4:
#         print("div is ", div(x, y))
#     elif ch == 5:
#         print("floor is ", floor(x, y))
#     else:
#         print("not valid")
#         break

# def prime(n):
#     b = []
#     for i in range(2, n + 1):
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 b.append(i)
#     return b
#
#
# x = int(input("enter the limit"))
# print("prime numbers", prime(x))


# x = input("enter the word")
# c = ""
# for i in x:
#     if i not in "aeiouAEIOU":
#         c += i
# print(c)

# x=[i for i in range(1,101) if i % 5 ==0]
# print(x)


# x = [1,0,7,5,9,2,3,5,7,2,0,1,10]
# x= list(dict.fromkeys(x))
# print(x)
