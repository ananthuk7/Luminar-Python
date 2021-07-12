f = open("firstFile", "r")

count = 0

words = {}
for i in f:
    strings = i.rstrip('\n').split(" ")

    for j in strings:
        words[j] = strings.count(j)
print(words)
