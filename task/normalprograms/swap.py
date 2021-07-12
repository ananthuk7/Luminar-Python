num1 = int(input("enter number"))
num2 = int(input("enter number"))

# 1st method

temp = num1
num1 = num2
num2 = temp
print(num1, num2)
# 2nd method

num1, num2 = num2, num1

print(num1, num2)

# 3rd method

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1, num2)

# 4th method

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print(num1, num2)
