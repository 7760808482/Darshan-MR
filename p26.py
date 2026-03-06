class Vehicle:
    def __init__(self,brand,rent_per_day):
        self.brand=brand
        self.rent_per_day=rent_per_day
    def calculate_rents(self,days):
        return self.rent_per_day*days
    def display(self):
        print("vehicle brand:",self.brand)
class Car(Vehicle):
    def __init__(self,brand,rent_per_day,seats):
        super().__init__(brand,rent_per_day)
        self.seats=seats

    def display(self):
        super().display()
        print("seats:",self.seats)
class Bike(Vehicle):
    def __init__(self,brand,rent_per_day,gear):
        super().__init__(brand,rent_per_day)
        self.gear=gear
    def display(self):
        super().display()
        print("gear:",self.gear)   
v1=Car("toyota",2000,5)
v2=Bike("yamaha",1000,150)
vehicles=[v1,v2]
for v in vehicles:
    v.display()
    print("rent for 3 days:",v.calculate_rents(3))
     
        
