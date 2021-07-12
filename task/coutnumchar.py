x = "abc123"
num = "1234567890"
countn, counts = 0, 0
for i in x:
    if i == " ":
        continue
    elif i in num:
        countn += 1
    else:
        counts += 1
print("number count", countn)
print("string count", counts)
