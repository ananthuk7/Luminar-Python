# import re
#
# n = "hello"
#
# r = "\w*"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")



# import re
#
# n = "56kg"
#
# # r = "[0-9a-z]+"
# r="[5][6][k][g]"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


#
# import re
# # Abc1 aaaa1 CC1
# n = input("enter the string ")
#
# r = "[a-zA-Z]+\d{1}$"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#
# import re
# # abcb  ab
# n = input("enter the string ")
#
# r = "^a[a-zA-Z0-9\W]*b$"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")



# import re
# # minimum 8-maximum 15
# # no digits
# n = input("enter the string ")
#
# r = "\D{8,15}"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


# import re
# # starting with uppercase A
# # numbers lowercase symbols
# n = input("enter the string ")
#
# r = "[A-Z]{1}[a-z0-9\W*]"
# match=re.fullmatch(r,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")



