class Bank:
    bank_name = "sbi"

    def details(self, name, amount):
        self.name = name
        self.amount = amount

    def withdrawal(self, b_amount):
        if self.amount > b_amount:
            withdrawalAmount = self.amount - b_amount
            print(withdrawalAmount)

        else:
            print("insufficient balance")

    def addito(self, a_amount):
        self.amount = self.amount + a_amount
        print("your account have rs", self.amount)


obj1 = Bank()
obj1.details("ananthu", 50000)
obj2 = Bank()
obj2.details("ananth", 500000)
obj3 = Bank()
obj3.details("anant", 5000)

while True:
    print("bank name", Bank.bank_name)
    a = input("enter the name")
    if obj1.name == a:
        print("your account have rs", obj1.amount)
        print("1.withdraw\n 2.deposit \n 3.exit")
        ch = int(input("enter your choice"))
        if ch == 1:
            b = int(input("enter the amount to withdraw"))
            obj1.withdrawal(b)
            continue
        elif ch == 2:
            c = int(input("enter the amount to deposit"))
            obj1.addito(c)
            continue
        elif ch == 3:
            break
    elif obj2.name == a:
        print("your account have rs", obj2.amount)
        print("1.withdraw\n 2.deposit \n 3.exit")
        ch = int(input("enter your choice"))
        if ch == 1:
            b = int(input("enter the amount to withdraw"))
            obj2.withdrawal(b)
            continue
        elif ch == 2:
            c = int(input("enter the amount to deposit"))
            obj2.addito(c)
            continue
        elif ch == 3:
            break
    elif obj3.name == a:
        print("your account have rs", obj3.amount)
        print("1.withdraw\n 2.deposit")
        ch = int(input("enter your choice"))
        if ch == 1:
            b = int(input("enter the amount to withdraw"))
            obj3.withdrawal(b)
            continue
        elif ch == 2:
            c = int(input("enter the amount to deposit"))
            obj3.addito(c)
            continue
        elif ch == 3:
            break
    else:
        print("you dont have any account")
