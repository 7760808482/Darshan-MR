class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added")

    def display(self):
        print("\nSavings Account Details")
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {new_balance}")
        else:
            print("Overdraft limit exceeded")

    def display(self):
        print("\nCurrent Account Details")
        super().display()
        print(f"Overdraft Limit: {self.overdraft_limit}")


def main():
    acc1 = SavingsAccount("Anita", 10000, 5)
    acc2 = CurrentAccount("Rahul", 5000, 2000)

    accounts = [acc1, acc2]

    for acc in accounts:
        acc.display()

    print("\nTransactions:")
    acc1.add_interest()
    acc2.withdraw(6000)


if __name__ == "__main__":
    main()