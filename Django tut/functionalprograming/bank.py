# users = {
#     1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
#     1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
#     1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
#     1003: {"acconu_num": 1003, "password": "user4", "balance": 6000},
# }
#
#
# #  want to check 1000 is exit or not then print the balance of 1000
# # if 1000 in users:
# #     print(users[1000]["balance"])
# #
#
# def authenticate(**kwargs):
#     user = kwargs["accountno"]
#     password = kwargs["password"]
#     if user in users:
#         if password == users[user]["password"]:
#             print("valid user")
#     else:
#         print("invalid user")
#
#
# def balance(account):
#     if account in users:
#         print(users[account]["balance"])
#
#
# authenticate(accountno=1000, password="user1")
# balance(account=1000)

# python uses snake notation
class Bank:
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user4", "balance": 6000},
    }
    session = {}

    def vaildate(self, accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):
        acc_no = kwargs["acc_no"]
        password = kwargs["password"]
        valid = self.vaildate(acc_no)
        if valid:
            if password == self.users[acc_no]["password"]:
                self.session["user"] = acc_no
                return acc_no
            else:
                return -1
        else:
            return 0

    def balance_enquiry(self, accno):
        if accno == self.session["user"]:
            print(self.users[accno]["balance"])
        else:
            print("please login")

    def fund_transfer(self, **kwargs):
        user_acc = kwargs["user_accno"]
        receiver = kwargs["receiver_acc"]
        amt = kwargs["amount"]
        if self.vaildate(receiver):
            balance = self.users[user_acc]["balance"]  # 4000
            if balance > amt:  # 4000 > 1000
                self.users[user_acc]["balance"] -= amt
                self.users[receiver]["balance"] += amt
            else:
                print("insufficient balance")
        else:
            print("invalid receiver")


obj = Bank()
user = obj.authenticate(acc_no=1001, password="user2")
if user == -1 or user == 0:
    print("authentication failed")
else:
    obj.balance_enquiry(user)
    obj.fund_transfer(user_accno=user, receiver_acc=1000, amount=1000)
    obj.balance_enquiry(user)

# obj1 = Bank()
# user = obj1.authenticate(acc_no=1000, password="user1")
# if user == -1 or user == 0:
#     print("authentication failed")
# else:
#     obj1.balance_enquiry(user)
