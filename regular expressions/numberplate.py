import re
r = "[K][F]\d{2}[A-Z]{2}\d{4}"
f = open("numberplate", "r")
f1 = open("crtnum", "a")
for i in f:
    valid=i.rstrip("\n")

    match = re.fullmatch(r, valid)

    if match != None:

        f1.write(i)
