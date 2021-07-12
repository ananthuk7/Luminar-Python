# quantifiers

# x='a+' a including group
# x='a*' count including zero number of abc
# x= 'a?' count a as each including zero no of abc
# x= 'a{2}' 2 number of position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x= 'a$' check ending with a


import re

# 1

# x = "a+"
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# 2

# x = "a*"  # it also check zero positions
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# 3

# x = "a?"
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# 4

# x = "a{2}"
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# 5

# x = "a{2,3}"
# r = "aa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# 6

# x = "^a"
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# 7

# x = "a$"
# r = "aaa abc aaa aaa"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
