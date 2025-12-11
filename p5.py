print("Enter your name")
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))
percentage = (marks_obtained / total_marks) * 100
print(f"Your percentage is: {percentage}%")
if percentage >= 85:
    print("Result: Distinction")
elif percentage >= 60:
    print("Result: First Class")
elif percentage >= 40:
    print("Result: Second Class")
else:
    print("Result: Fail")
