def find_divisible_numbers(numbers, divisor):
    divisible_numbers = []
    for number in numbers:
        if number % divisor == 0:
            divisible_numbers.append(number)
    return divisible_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 5

divisible_numbers = find_divisible_numbers(numbers, divisor)
print(f"Numbers divisible by {divisor}: {divisible_numbers}")