# Program to find factorial of a number in Python using function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is negative
if num < 0:
    print("Factorial cannot be calculated for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)