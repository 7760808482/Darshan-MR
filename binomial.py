def factorial(n):
 if n == 0 or n == 1:
 return 1
 else:
 result = 1
 for i in range(2, n + 1):
 result *= i
 return result
def binomial_coefficient(N, R):
 return factorial(N) // (factorial(R) * factorial(N - R))
N = int(input("Enter the value of N: "))
R = int(input("Enter the value of R: "))
if R > N:
 print("Invalid input. R must be less than or equal to N.")
else:
 binom_coeff = binomial_coefficient(N, R)
 print(f"Binomial Coefficient C({N}, {R}) = {binom_coeff}")