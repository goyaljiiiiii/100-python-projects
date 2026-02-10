# This is file number 10- temp converter

print("Choose one to covert")
print("1. Celsius ↔ Fahrenheit")
print("2. Fahrenheit ↔ Celsius ")


user_input=int(input("Enter the choice above(1,2): "))
if user_input==1:
    celsius=float(input("Enter the temperature in Celsius: "))
    fahrenheit=(celsius*9/5)+32 
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif user_input==2:
 fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
 celsius=(fahrenheit-32)*5/9
 print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
 print("Invalid choice")  # This will be printed if the user enters anything other than
