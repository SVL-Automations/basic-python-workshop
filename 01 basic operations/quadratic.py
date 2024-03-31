# Simple quadratic equation program in Python

import cmath

# Input coefficients from the user
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Calculate the solutions
solution1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
solution2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

# Print the solutions
print("The solutions are:")
print("Solution 1:", solution1)
print("Solution 2:", solution2)