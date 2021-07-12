import re

n = input("enter the vehile  number ")

r = "[K][L][0-9]{2}[A-Z]{2}\d{4}"
match = re.fullmatch(r, n)
if match is not None:
    print("valid")
else:
    print("not valid")