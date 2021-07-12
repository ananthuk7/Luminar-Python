list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

# <=== properties ===>

# support duplicate data's
# it keeps order
# heterogeneous
# nesting is possible
# mutable


# creating an empty list
list2 = []
print(type(list1))
list2.append("hello")
print(list2)
list2.append(8)
print(list2)

# iteration in list
for i in list1:
    print(i)

# remove an element
lst = [1, 4, 5, 99, 2, 55, 90, 7, 4, 1, 2, 3, 2, 1]
# clear a single element
lst.remove(1)
lst.remove(1)
lst.remove(1)

print("element removed", lst)

# clear all the element
lst.clear()
print(lst)

# remove the set

del lst

lst = [1, 2, 3, [4, 5, 6]]
print(lst)

# adding two list
lst = [1, 2, 3,]
lst1= [4, 5, 6]
lst.extend(lst1)
print(lst)

lst = [1, 2, 3,]
print(lst.pop())
print(lst)
