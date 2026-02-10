# This is file number 5-Fibonacci Series Generator

first_num = 0
second_num = 1
n = int(input("Enter the number of terms: "))

for num in range(n):  
    print(first_num)  # Print the current number
    sum = first_num + second_num  # Store the next number
    first_num = second_num  # Move first_num forward
    second_num = sum  # Move second_num forward
