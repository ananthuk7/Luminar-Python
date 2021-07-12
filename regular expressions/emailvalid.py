import re

rule = '[a-zA-Z]+[@][a-z]+[.]+[a-z]+'
e = input("enter mail")
matcher = re.fullmatch(rule, e)
if matcher is not None:
    print("valid")
else:
    print("not valid")
