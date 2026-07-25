from account import Account

# Create two accounts
acc1 = Account("Yoseph", "ACC001", 1000)
acc2 = Account("Abel", "ACC002")

print("Initial Balances")
print(acc1.balance)
print(acc2.balance)

print("Deposit")
acc1.deposit(500)
print(acc1.balance)      # 1500

print("Withdraw")
acc1.withdraw(300)
print(acc1.balance)      # 1200

print("Invalid Deposit")
try:
    acc1.deposit(-100)
except ValueError as e:
    print(e)

print("Invalid Withdrawal")
try:
    acc1.withdraw(-50)
except ValueError as e:
    print(e)

print("Overdraft")
try:
    acc1.withdraw(5000)
except ValueError as e:
    print(e)

print("Read only Property")
try:
    acc1.balance = 5000
except AttributeError as e:
    print(e)

print("Statement")
acc1.statement()
acc2.statement()

