class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def abc(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)

    def mod(self):
        print(self.num1 % self.num2)


x = int(input("enter the number"))
y = int(input("enter the number"))
cal = Calculator(x, y)
cal.div()
