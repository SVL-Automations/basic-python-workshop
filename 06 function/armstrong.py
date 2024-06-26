# Python program to check armstrong number or not

def is_armstrong_number(number):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    if sum_of_digits == number:
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")