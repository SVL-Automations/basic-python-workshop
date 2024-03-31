# Printing table in Python for given number using for loop and function

def print_multiplication_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage
num = int(input("Enter a number: "))
print_multiplication_table(num)