from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @abstractmethod
    def calculate_fee(self):
        pass

    @property
    def balance(self):
        return self._balance

class SavingsAccount(Account):
    def calculate_fee(self):
        return self.balance * 0.01

class CurrentAccount(Account):
    def calculate_fee(self):
        return 5.0

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

accounts = [SavingsAccount(1000), CurrentAccount(500)]
for acc in accounts:
    print(acc.calculate_fee())