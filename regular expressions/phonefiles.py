import re

rule = "[+][9][1][0-9]{10}"
f = open("phone", "r")
for num in f:
    number=num.rstrip("\n")
    matcher = re.fullmatch(rule, number)
    if matcher is not None:
        print(number)
