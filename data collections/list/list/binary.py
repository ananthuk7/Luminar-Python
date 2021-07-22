def binarySe(a, k):  # [4,5,6] ,4
    length = len(a)  # 3
    lo = 0  # 0
    high = length - 1  # 2
    flg = 0
    while lo <= high:  # 0<= 2 #2<=2  #0 <= 0
        mid = (lo + high) // 2  # mid= 0+2//2=1  2+2//2=2  0/2
        # print(mid)
        if k > a[mid]:  # 6 >  a[mid]=5  6> 6   4>4
            lo = mid + 1  # lo=1+1=2
        elif k < a[mid]:  # 6<6   4 < a[1]=5
            high = mid - 1  # h=1-1
        elif k == a[mid]:  # 6==6
            flg = 1
            break

    if flg == 1:
        print("found")
    else:
        print("not found")


li = [6, 5, 4, 3, 2, 1]

# for i in range(0, len(li)):
#     for j in range(i + 1, len(li)):
#         if li[i] > li[j]:
#             li[i], li[j] = li[j], li[i]
# print(li)
li.sort()
binarySe(li, 1)
