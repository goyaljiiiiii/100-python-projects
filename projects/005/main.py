# This is file number 5-factorial calculator

number = int(input("Enter a number: "))
factorial = 1

for num in range(1, number + 1):
    factorial *= num

print("Factorial of", number, "is", factorial)  
