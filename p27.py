class Person:
    def __init__(self, name, age):
        # Encapsulation (data hiding using private variable)
        self.name = name
        self.__age = age      # private attribute

    # Getter method (access private data)
    def get_age(self):
        return self.__age

    # Method
    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")


# Derived Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Calling parent constructor
        super().__init__(name, age)
        self.student_id = student_id

    # Method Overriding (Polymorphism)
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.get_age()}")
        print(f"Student ID: {self.student_id}")


# Another Derived Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Polymorphism
    def display(self):
        print(f"Teacher Name: {self.name}")
        print(f"Age: {self.get_age()}")
        print(f"Subject: {self.subject}")


# -------------------------------
# Main Program
# -------------------------------
def main():
    # Creating objects
    s1 = Student("Alice", 20, "S101")
    t1 = Teacher("Dr. Kumar", 45, "Mathematics")

    # Polymorphism in action
    people = [s1, t1]

    for person in people:
        person.display()
        print("------------------")


# Program execution
if __name__ == "__main__":
    main()