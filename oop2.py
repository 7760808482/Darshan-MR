#Abstraction

class car:
    def start_engine(self):
        print("Engine is started")
    def accelerate(self):
        print("car is accelerating")
    def breake(self):
        print("Car is stop")
cars=car()
cars.start_engine()
cars.accelerate()
cars.breake()
print()



class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def check_balance(self):
        return self.balance
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f"Withdraw ammount:{amt},\tNew balance:{self.balance}")
        else:
            print("Insufficient balance")
    def deposit(self,amt):
        self.balance+=amt
        print(f"Deposited ammount:{amt},\tNew balance:{self.balance}")
BA=BankAccount(911,100000)
BA.deposit(500)
BA.withdraw(100)
print("The New Blanance:",BA.check_balance())
print()



class ATM:
    def __init__(self,balance):
        self.balance=balance
    def deposite(self,amt):
        self.balance+=amt
        print(f"Deposited {amt}.\nNew balance: {self.balance}")
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f"Withdrew {amt}.\n New balance: {self.balance}")
        else:
            print("Insufficient balance")
    def cheack_balance(self):
        return self.balance
atm=ATM(1000)
atm.deposite(500)
atm.withdraw(100)
atm.cheack_balance()


#Encapsulation

class Database:
    def __init__(self):
        self.__storage={}                 #private variable(__storage). we use the double "__"
    def write(self,key,values):
        self.__storage[key]=values
        print(f"Data saved for {key}")
    def get_data(self,key):
        return self.__storage.get(key,"no data found")
db=Database()
db.write("user1",{"name":"Drashan","age":19})
print(db.get_data("user1"))
print(db._Database__storage) 
print()


