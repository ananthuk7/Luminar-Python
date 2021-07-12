# set

set1 = {1, 4, 5, 99, 2, 55, 90, 7, 4, 1, 2, 3, 2, 1}
print(set1)
print(type(set1))

#  <===FEATURES===>

# doesnt store duplicate elements
# order doesn't keep
# heterogeneous data collection
# set is a mutable data collection
# nesting is not possible

# <===property of sets===>


# add an element
s = set()  # initialize a set
s.add("hello")
s.add(9)
s.add(True)
print(s)

# remove an element
set2 = {1, 4, 5, 99, 2, 55, 90, 7, 4, 1, 2, 3, 2, 1}
# clear a single element
set2.remove(1)
print("element removed", set2)

# clear all the element
set2.clear()
print(set2)

# remove the set

del set2

set2 = {1, 4, 5, 99, 2, 55, 90, 7, 4, 1, 2, 3, 2, 1}

# for copy an element
set3 = set2.copy()
print("copied set is", set3)

# set operations
a = {1, 2, 3, 4, 5}
b = {1, 2, 7, 8}

# union
print(a.union(b))
# intersection
print(a.intersection(b))
# difference
print(a.difference(b))
