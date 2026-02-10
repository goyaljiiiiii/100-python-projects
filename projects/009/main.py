# This is file number 9- Convert Decimal to Binary

user_num = int(input("Enter a number: "))

quotient = user_num  # Start with the given number
binary = ""  # Store binary result as a string

while quotient > 0:  # Keep dividing until quotient is 0
    remainder = quotient % 2  # Get remainder (0 or 1)
    binary = str(remainder) + binary  # Add remainder to the left
    quotient = quotient // 2  # Integer division to update quotient

print("Binary:", binary)
