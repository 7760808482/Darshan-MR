'''Constructor (__init__) should take:
name
balance
Create a method deposit(amount):
Add amount to balance
Create a method withdraw(amount):
If balance is enough → subtract amount
Else → print "Insufficient balance"
Create a method display():'''

class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,ammt):
        self.balance=self.balance+ammt
    def withdraw(self,ammt):
        if self.balance>=ammt:
            self.balance=self.balance-ammt
        else:
            print("Insufficient balance")
    def display(self):
        print("Name:",self.name)
        print("Ammount:",self.balance)
amt=bank("Darshan",5000)

amt.deposit(150)
amt.withdraw(3000)
amt.display()