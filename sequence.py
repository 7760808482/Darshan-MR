N = int(input("Enter the length of the Fibonacci sequence: "))
a, b = 0, 1
if N <= 0:
 print("Please enter a positive integer.")
elif N == 1:
 print(f"Fibonacci sequence of length {N}: {a}")
else:
 print(f"Fibonacci sequence:")
 print(a, b, end=" ")
 for i in range(2, N):
     next_number = a + b
 print(next_number, end=" ")
 a, b = b, next_number