name = input("Enter Student Name: ")
usn = input("Enter Student USN: ")
marks1 = int(input("Enter the marks in subject 1: "))
marks2 = int(input("Enter the marks in subjec 2: "))
marks3 = int(input("Enter the marks in subject 3: "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100
print()
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
