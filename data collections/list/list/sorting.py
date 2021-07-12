# li = [1, 3, 2, 4, -1, -2, -3]
# print(li.sort())
#
# for i in range(0, len(li) - 2):
#     for j in range(i + 1, len(li) - 1):
#         if li[i] > li[j]:
#             li[i], li[j] = li[j], li[i]
#
# print(li)
#
# # 0 1 2 3 4
# # 1 2 3 4
# # 2 3 4
# # 3 4
myList = [6, 5, 4, 3, 2, 1]
newList = []

while myList:
    minVal = myList[0]
    for i in myList:
        if i < minVal:
            minVal = i
    newList.append(minVal)
    myList.remove(minVal)
print(newList)

# x = [1, 25, 4, 554, 664, 11, 778, 54]
# y = []
# for i in x:
#     print("value of i ", i, end=" ")
#     print('\n')
#     mim = x[0]
#     print("min", mim, end=" ")
#     print('\n')
#     for j in x:
#         print("value of j ", j, end=" ")
#         print('\n')
#         if j < mim:
#             mim = j
#             print("min", mim, end=" ")
#             print('\n')
#     y.append(mim)
#     x.remove(mim)
# print(y)
