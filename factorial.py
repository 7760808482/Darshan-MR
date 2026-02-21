'''You have to complete a function named factorial which will return the factorial of the integer N.
Note: Main code is already implemented, you need to complete the factorial function only.'''
#Return the factorial of the number N
def factorial(N):
    # Your code goes here
    if N==0 or N==1:
        return 1
    else:
        return(N*factorial(N-1))
    return