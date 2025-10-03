# Program to check if the given string is a palindrome

def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    # Check if string is equal to its reverse
    return string == string[::-1]

# Input from user
text = input("Enter a string: ")

# Check and display result
if is_palindrome(text):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")