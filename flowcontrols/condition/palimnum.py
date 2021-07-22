# def rev(num):  #121
#     rev1 = 0
#     while num > 0:  # 121 > 0 12 >0 1 >0  .1 >0
#         r = num % 10   # 121 % 10  12 % 10  1%10
#
#         rev1 = (rev1*10)+r # 0*10 +1  1*10+2 =12  12*10 +1
#
#         num = num // 10  #121/10 => 12.1 12/10 1.2  1/10 .1
#     return rev1
#
#
x = int(input("enter the number")) #121
# y = rev(x)
# # print(y)
# if x == y:
#     print("palindrome")
# else:
#     print("not palindrome")

y=str(x)
# print(y[::-1])
if y == y[::-1]:
    print("palim")
else:
    print("not")