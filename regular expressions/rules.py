# Rules

# x='[abc]' either a b or c
# x='[^abc]' expect abc
# x='[a-z]'  a to z
# x='[A-Z]'  A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all the words except special characters
# x='\W' for special characters


import re
# 1
# x = "[abc]"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# # 2
# x = "[^abc]"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# # 3
# x = "[a-z]"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# # 4
# x = "[A-Z]"
# matcher = re.finditer(x, "ABC @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# # 5
# x = "[a-zA-z]"
# matcher = re.finditer(x, "ABC @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# # 6
# x = "[0-9]"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# # 7
# x = "[a-zA-Z0-9]"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# x = "\s"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# x = "\d"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# x = "\D"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# x = "\w"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# x = "\W"
# matcher = re.finditer(x, "abc @12assdags")
# for match in matcher:
#     print(match.start())
#     print(match.group())




