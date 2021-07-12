x = "hello"
y = "lbo"
s = ""
for i in x:
    if i in y:
        s = s + i
if s == "":
    print("no common")
else:

    print("common")
