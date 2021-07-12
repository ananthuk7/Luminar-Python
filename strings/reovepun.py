x = '''"!@#$%^&*()_+/~`,.[]{} '''
b = input("enter the string")
c = ""
for i in b:
    if i not in x:
        c += i

print(c)
