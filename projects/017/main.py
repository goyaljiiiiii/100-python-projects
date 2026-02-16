import random

options = ("Rock", "Paper", "Scissors")

print("\n🎮 Welcome to the Ultimate Rock-Paper-Scissors Battle! 🎮")
print("👊 Rock  📄 Paper ✂ Scissors")
print("Type 'q' anytime to surrender like a weakling. 😜\n")

while True:
    user_guess = input("👉 Choose your weapon (Rock/Paper/Scissors): ").capitalize()

    if user_guess.lower() == "q":
        print("😢 You ran away! The computer wins by default. Try again next time! 🤖🏆")
        break

    if user_guess not in options:
        print("🤦‍♂️ Invalid move! Are you trying to invent a new option? Try again!")
        continue

    one = random.choice(options)
    print(f"🖥 Computer chose: {one}")

    if user_guess == one:
        print("😮 It's a draw! Are we telepathic or what?!")
    elif (
        (user_guess == "Rock" and one == "Scissors")
        or (user_guess == "Paper" and one == "Rock")
        or (user_guess == "Scissors" and one == "Paper")
    ):
        print("🎉 YOU WIN! The computer is crying in binary. 🤖💀")
    else:
        print("💀 LOL, you lost! The computer is flexing its AI muscles. 🤖💪")

    print("\n⚔ Ready for another round? Bring it on! ⚡\n")
