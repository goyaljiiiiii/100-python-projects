import random

word_categories = {
    "fruits": ["apple", "banana", "mango", "grape", "cherry", "orange", "pineapple", "strawberry", "watermelon", "papaya"],
    "animals": ["elephant", "giraffe", "tiger", "kangaroo", "panda", "dolphin", "zebra", "crocodile", "rhinoceros", "peacock"],
    "countries": ["india", "canada", "brazil", "germany", "france", "japan", "italy", "australia", "mexico", "argentina"],
    "sports": ["football", "cricket", "badminton", "basketball", "volleyball", "hockey", "tennis", "wrestling", "golf", "swimming"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange", "black", "white", "brown", "pink"]
}


def printingAndAsking():
    print("\nCummon, Choose either of the categories:\n")
    print(" 1. Fruits \n 2. Animals \n 3. Countries  \n 4. Sports  \n 5. Colors\n")

    while True:
        try:
            choosen = int(input("Choose a category (1-5): "))
            if 1 <= choosen <= 5:
                return choosen
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            choosen = int(input("Now dont play and Choose a category (1-5): "))


def randomChoice(choosen):
    changeNumToCategories = {
        1: "fruits",
        2: "animals",
        3: "countries",
        4: "sports",
        5: "colors"
    }
    category = changeNumToCategories[choosen]
    pickWord = random.choice(word_categories[category])
    print("")
    print(f"You chose {category}. Let's begin!")
    return pickWord


def mainFunc(pickWord):
    guessed_letters = set()
    hidden_word = ["_"] * len(pickWord)
    attempts = 6

    while attempts > 0 and "_" in hidden_word:
        print("\nWord: " + " ".join(hidden_word))
        userInput = input("Enter a letter: ").lower()

        if len(userInput) != 1 or not userInput.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if userInput in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(userInput)

        if userInput in pickWord:
            for i in range(len(pickWord)):
                if pickWord[i] == userInput:
                    hidden_word[i] = userInput
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

    if "_" not in hidden_word:
        print("\nCongratulations! You guessed the word:", pickWord)
    else:
        print("\nGame over! The word was:", pickWord)


# Execution
choosen_category = printingAndAsking()
selected_word = randomChoice(choosen_category)
mainFunc(selected_word)
