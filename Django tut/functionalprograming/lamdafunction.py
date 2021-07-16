# lamda function

# def add(num1,num2):
#     return num1+num2
#
# print(add(5,6))
#
# add = lambda num1, num2: num1 + num2
# print(add(5,6))

# lst = [1, 2, 3, 4, 5, 6, 7]

# sq=[]
# for i in lst:
#     sq.append(i**2)
# print(sq)


# map(function,itreatable)


# def square(num1):
#     return num1 ** 2
#
#
# squares = list(map(square, lst))
# print(squares)


# squares = list(map(lambda num1: num1 ** 2,lst))
# print(squares)







#print all product details availave <250

# pd = list(filter(lambda product:product["mrp"]<250,products))
# print(pd)




#num1=10
#num2=20
# res=num1 if num1>num2 else num2

#num=1
#res="odd" if num%2!=0 else "even"

#num2
#res="+ve" if num >0 else "-ve"


# #lst =[2,3,4,8,10,7] if num<5 num-1 else num+1
# lst =[2,3,4,8,5,10,7]
# # op=[]
# # for i in lst:
# #     if i <5:
# #         op.append(i-1)
# #     else:
# #         op.append(i+1)
# # print(op)
#
# # op=list(map(lambda num:num+1 if num>5 else num-1,lst))
# # print(op)
#
# op=list(map(lambda num: num+1 if num>5 else num-1 if num <5 else num,lst))
# print(op)



#reduce
#dont have enough reach

# from functools import  reduce
# lst=[1,2,3,4,5,6,7]
# total=reduce(lambda num1,num2:num1+num2,lst)
# print(total)

#largest
# largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(largest)


