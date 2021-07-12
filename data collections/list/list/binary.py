def binarySe(a, k):
    length = len(a)
    lo = 0
    high = length - 1
    flg = 0
    while lo <= high:
        mid = (lo + high) // 2
        print(mid)
        if k > a[mid]:
            lo = mid + 1
        elif k < a[mid]:
            high = mid - 1
        elif k == a[mid]:
            flg = 1
            break

    if flg == 1:
        print("found")
    else:
        print("not found")


li = [6, 5, 4, 3, 2, 1]

for i in range(0, len(li)):
    for j in range(i + 1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)
binarySe(li, 11)
