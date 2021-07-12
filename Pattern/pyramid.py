# x = int(input(" enter the limit"))
# for i in range(0, x):
#     k = x - i
#     for k in range(0, k):
#         print(' ',end=" ")
#         for j in range(0, 1):
#             print("*", end=" ")
#         k=k-1
#     print()
#
#
#     *
#    * *
#  * * * *

def pyramid(n):
    k = n
    for i in range(0, n):
        for r in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print('\r')


pyramid(10)

for i in range(0, 6):
    print(" " * (6 - i), end=" ")
    for j in range(0, i + 1):
        print('*', end=" ")
    print()
