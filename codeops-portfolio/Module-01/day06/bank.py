class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


class SMSAlert:
    def update(self, message):
        print(f"[SMS] {message}")


class AuditLog:
    def update(self, message):
        print(f"[Audit] {message}")


class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        self._balance += amount
        self._notify(f"Deposited {amount} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        self._notify(f"Withdrew {amount} ETB")

    def statement(self):
        print(f"{self.owner} | {self.number} | {self.balance} ETB")


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.rate = BankConfig().interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    def statement(self):
        print(f"Savings Account")
        super().statement()


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount
        self._notify(f"Withdrew {amount} ETB")

    def statement(self):
        print(f"Current Account")
        super().statement()


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Unknown account type")


acc1 = AccountFactory.create("savings", "Almaz", "ACC001", 2000)
acc2 = AccountFactory.create("current", "Dawit", "ACC002", 500)

sms = SMSAlert()
audit = AuditLog()

acc1.subscribe(sms)
acc1.subscribe(audit)

acc1.deposit(500)
acc1.withdraw(300)
acc1.add_interest()

acc1.statement()
acc2.statement()

config1 = BankConfig()
config2 = BankConfig()

print(config1 is config2)
