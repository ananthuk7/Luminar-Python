f = open("book", "r")
fi = open("firstFile", 'w')
for i in f:
    fi.write(i)
