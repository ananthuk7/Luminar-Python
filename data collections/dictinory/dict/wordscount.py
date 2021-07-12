# x = input("enter the sentance")
# y = x.split(" ")
# count = {}
# c = 0
# for i in y:
#     first = y[0]
#     if i == first:
#         c = c + 1
#     count[i] = c
# print(count)
#

# counter = {}
# dat = "hello hai hello"
# words = dat.split(" ")
# for word in words:
#     if word not in counter:
#         counter.update({word: 1})
#     else:
#         val = int(counter[word])
#         val += 1
#         counter.update({word: val})
# print(counter)


x = input("enter the sentence")
y = x.split(" ")
count1 = {}

for i in y:
    count1[i] = y.count(i)
print(count1)

