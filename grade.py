//InterviewBit Question: https://www.interviewbit.com/problems/grade-calculator
'''Given an integer num denoting percentage of a student, calculate the grade according to the below rules:

If num >= 90, grade A.
If num >= 80, grade B.
If num >= 70, grade C.
If num >= 60, grade D.
If num >= 50, grade E.
Else grade will be F.
Print a string consisting of single character denoting the grade.

Sample Input

59
Sample Output

E'''
def main():
    num = int(input())
    # YOUR CODE GOES HERE
    if num>=90:
        print("A")
    elif num>=80:
        print("B")
    elif num>=70:
        print("C")
    elif num>=60:
        print("D")
    elif num>=50:
        print("E")
    else:
        print("F")
    return 0

if __name__ == '__main__':
    main()
