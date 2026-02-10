# This is file number 3- Even odd calculator

while True:
    user_choice = input("Enter a number to test (q to quit): ")

    # Check if user wants to quit
    if user_choice.lower() == "q":
        print("Goodbye!")
        break

    try:
        # Convert input to integer and check even/odd
        number = int(user_choice)
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    except ValueError:
        print("Invalid input, please enter a valid number or 'q' to quit.")
