class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.history.append(-amount)

    def statement(self):
        print(f"{self.owner}")
        print(f"{self.account_number}")
        print(f"{self.balance} ETB")
        print()


def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def recursive_sum(values):
    if not values:
        return 0

    return values[0] + recursive_sum(values[1:])


class AccountRegistry:

    def __init__(self):
        self.by_number = {}

    def add(self, account):
        self.by_number[account.account_number] = account

    def top_by_balance(self, n=5):
        accounts = sorted(
            self.by_number.values(),
            key=lambda account: account.balance,
            reverse=True
        )

        return accounts[:n]

    def find_by_number(self, number):
        numbers = sorted(self.by_number.keys())

        index = binary_search(numbers, number)

        if index == -1:
            return None

        return self.by_number[numbers[index]]

    def total_transactions(self, number):
        account = self.find_by_number(number)

        if account is None:
            return None

        return recursive_sum(account.history)


registry = AccountRegistry()

a1 = Account("Almaz", "ACC001", 2500)
a2 = Account("Dawit", "ACC002", 1800)
a3 = Account("Hanna", "ACC003", 3200)

registry.add(a1)
registry.add(a2)
registry.add(a3)

a1.deposit(500)
a1.withdraw(200)
a1.deposit(300)

print("Top Accounts")

for account in registry.top_by_balance(2):
    account.statement()

found = registry.find_by_number("ACC002")

if found:
    found.statement()

print("Transaction Total:")
print(registry.total_transactions("ACC001"))