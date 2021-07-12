# pattern matching


# re ==> used for pattern matching


import re

count = 0
matcher = re.finditer("ab", "ababbbabbabaabab")

for match in matcher:
    print("match available at",match.start())
    print("matching group",match.group())
    count += 1
print(count)
