bankDeposit = 10000
withDrawlAmount = int(input("Enter the amount taken "))
if withDrawlAmount <= bankDeposit:
    currentAmount = bankDeposit - withDrawlAmount
    print("current balance", currentAmount)
else:
    print("insufficient balance")
