class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []  # Transaction stack (LIFO)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        self.history.append(("withdraw", amount))

    def undo_last(self):
        if not self.history:
            print("No transactions to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self.balance -= amount
            print(f"Undid deposit of {amount} ETB")

        elif action == "withdraw":
            self.balance += amount
            print(f"Undid withdrawal of {amount} ETB")

    def statement(self):
        print("-" * 35)
        print(f"Owner          : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.balance:.2f} ETB")
        print("-" * 35)


class AccountRegistry:
    def __init__(self):
        # Dictionary for O(1) lookup
        self.by_number = {}

        # List to preserve insertion order
        self.order = []

    def add(self, account):
        if account.account_number in self.by_number:
            raise ValueError("Account already exists.")

        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        return [self.by_number[number] for number in self.order]


# ----------------------------
# Testing the Program
# ----------------------------

registry = AccountRegistry()

acc1 = Account("Almaz", "ACC001", 2000)
acc2 = Account("Dawit", "ACC002", 1500)
acc3 = Account("Hanna", "ACC003", 3500)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

acc1.deposit(500)
acc1.withdraw(300)
acc1.deposit(200)

print("Before Undo")
acc1.statement()

acc1.undo_last()

print("\nAfter Undo")
acc1.statement()

print("\nFind Account ACC002")
account = registry.find("ACC002")

if account:
    account.statement()
else:
    print("Account not found.")

print("\nAll Accounts")

for account in registry.list_all():
    account.statement()