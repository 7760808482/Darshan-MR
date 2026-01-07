number = input("Enter a multi-digit number: ")
frequency = {}
for digit in number:
 if digit in frequency:
 frequency[digit] += 1
 else:
 frequency[digit] = 1
print("Digit frequency in the number:")
for digit, count in frequency.items():
 print(f"Digit {digit}: {count} times")