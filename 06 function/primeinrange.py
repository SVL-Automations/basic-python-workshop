# Print all prime numbers in a given range in Python

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking input from the user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Printing prime numbers within the range
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end+1):
    if is_prime(num):
        print(num)