# def pat1(li, c):
#     for k in range(0, li + 1):
#         for j in range(0, k):
#             print(c, end=" ")
#         print('\r')
#
#
# def pat2(li, c):
#     for i in range(li, -1, -1):
#         for j in range(0, i):
#             print(c, end=" ")
#         print('\r')


a = int(input("enter the initial element"))
b = int(input("enter the limit"))

# for i in range(b):
#     if a < b:
#         if a % 2 != 0:
#             pat1(b, a)
#             a += 1
#         else:
#             pat2(b, a)
#             a += 1
#

for i in range(b):
    if a < b:
        if a % 2 != 0:
            for k in range(0, b + 1):
                for j in range(0, k):
                    print(a, end=" ")
                print('\r')
            a += 1
        else:
            for i in range(b, -1, -1):
                for j in range(0, i):
                    print(a, end=" ")
                print('\r')
            a += 1
