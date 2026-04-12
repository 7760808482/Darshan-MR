'''Problem Description

We had discussed about filter. Let's try a question using it.

You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.
Input Format

The first line of input is the integer N, the number of email addresses.

N lines follow, each containing a string.

Output Format

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

Example Input

3
sara@scaler.com
brian-23@scaler.com
brute_54@scaler.com
Example Output

['brian-23@scaler.com', 'brute_54@scaler.com', 'sara@scaler.com']'''
#YOUR CODE GOES HERE
import re

def is_valid(email):
    # Regex Breakdown:
    # ^[a-zA-Z0-9_-]+  : Starts with one or more letters, digits, _, or -
    # @                : Followed by the @ symbol
    # [a-zA-Z0-9]+     : Followed by one or more letters or digits (website)
    # \.               : Followed by a dot
    # [a-zA-Z]{1,3}$   : Ends with 1 to 3 letters (extension)
    
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

def main():
    try:
        n = int(input().strip())
    except EOFError:
        return

    emails = []
    for _ in range(n):
        emails.append(input().strip())

    # Use filter to keep only valid emails
    # filter(function, iterable)
    valid_emails = list(filter(is_valid, emails))
    
    # Sort the list to meet lexicographical order requirement
    valid_emails.sort()
    
    print(valid_emails)

if __name__ == '__main__':
    main()