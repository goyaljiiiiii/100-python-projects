# This is file number 5- Prime number checker in a given range

user_input = int(input("Enter the range: "))  # Get the range

for num in range(2, user_input + 1):  # Loop through numbers in range
    is_prime = True  # Assume number is prime

    for i in range(2, num):  # Check divisibility
        if num % i == 0:
            is_prime = False  # If divisible, it's not prime
            break  # Exit loop early

    if is_prime:
        print(num, "is a prime number")  # Print the prime number
