import random

# Symbols for the slot machine
symbols = ["🍒", "7️⃣", "⭐", "💎", "🍋"]

def spin():
    result = []
    for _ in range(3):
        random_symbol = random.choice(symbols)
        result.append(random_symbol)
    return result

def check_win(reels):
    if reels[0] == reels[1] == reels[2]:
        return "🎉 JACKPOT! You just became rich... kinda!"
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return "🥈 You won a small prize! Enough for a cheap coffee."
    else:
        return "❌ Oof, you lost! Hope you didn’t bet your rent money."

# Main game loop
print("🎰 Welcome to the Totally-Not-Rigged Casino! 🎰")

while True:
    input("\nPress Enter to spin... (or rethink your life choices) 😅")
    result = spin()
    print(" | ".join(result))
    print(check_win(result))

    play_again = input("\nWanna go broke again? (y/n): ")
    if play_again.lower() != 'y':
        print("\nThanks for playing! Go touch some grass. 👋")
        break
