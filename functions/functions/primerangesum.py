n = int(input("enter the limit"))
sum = 0
for i in range(2, n + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sum = sum + i
print(sum)

# min=int(input("enter the limit"))
# max=int(input("enter the end"))
# sum=0
# for a in range(min,max):
#     if a>1:
#         for i in range(2,a):
#             if a%i==0:
#                 break
#         else:
#             sum=sum+a
# print(sum)
