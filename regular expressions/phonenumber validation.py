# import re
#
# n = input("enter the mobile number ")
#
# r = "[0-9]{10}"
# match = re.fullmatch(r, n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")
#

#indian mobile numbers
import re

n = input("enter the mobile number ")

r = "[+][9][1][0-9]{10}"
match = re.fullmatch(r, n)
if match is not None:
    print("valid")
else:
    print("not valid")
