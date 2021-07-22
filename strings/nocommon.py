x = "hello"
y = "lbo"
s = ""
for i in x:   # h  e  l  l  o
    if i not in y: # h not in  lbo
        s=s+i  #s= ""+h +e
print(s)
