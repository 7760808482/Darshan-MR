class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        print("Name of the student:",self.name)
        print("Marks of the student:",self.marks)

r1=student("Darshan",90 )
r1.result()
print()

'''Create a Class with a Constructor:

Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie’s title and rating.'''
class movie:
    def __init__(self,title,rating):
        self.rating=rating
        self.title=title

    def display(self):
        print(f"The title of the movie is {self.title} and the users rating of the movie is {self.rating}")
        
r1=movie("KGF",9)
r1.display()

'''Add Default Parameters:

Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
Write a method that displays the details of each employee.
Create multiple Employee objects with different values for name and designation, and test the default salary behavior.'''

class employee:                                                            #Attribute
    def __init__(self,name,desgination,salary=30000):
        self.name=name
        self.desgination=desgination
        self.salary=salary

    def display(self):
        print(f"Name of the Employee {self.name}")
        print(f"Desigation of the Employee {self.desgination}")
        print(f"Salary of thr Employee {self.salary}")

emp1=employee("Darshan","Developer",150000)                              #method
emp2=employee("Pavan","Doctor",600000)
emp3=employee("Prathibha","HR",450000)

emp1.display()
emp2.display()
emp3.display()
