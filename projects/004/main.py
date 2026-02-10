# This is file number 4 - Number Guessing Game

import random

# Generate a random number between 1 and 100
computer_choice = random.randint(1, 100)
tries = 0

while True:
    # Get user input
    try:
        user_choice = int(input("Guess the number between 1-100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    tries += 1  # Count the attempt

    # Check the guess
    if user_choice > computer_choice:
        print("Too high! Try again.")
    elif user_choice < computer_choice:
        print("Too low! Try again.")
    else:
        print(f"🎉 You guessed it! It took you {tries} tries.")
        break
