first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

first_list = []
second_list = []
common_divisors = []

# Find divisors of first number
for num in range(1, first_num + 1):
    if first_num % num == 0:
        first_list.append(num)

# Find divisors of second number
for num in range(1, second_num + 1):
    if second_num % num == 0:
        second_list.append(num)

# Find common divisors
for divisor in first_list:
    if divisor in second_list:
        common_divisors.append(divisor)

# Print the largest common divisor (GCD)
gcd = max(common_divisors)  # Pick the largest one
print(f"The GCD of {first_num} and {second_num} is {gcd}")
