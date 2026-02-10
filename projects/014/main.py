balance = 0  # Global balance variable


def main():
  print("\nWhat would you like to do?")
  print("1. Check your broke-ness")
  print("2. Flex—I mean, Deposit money")
  print("3. Go bankrupt—I mean, Withdraw money")
  print("4. Escape this financial crisis")


def current_balance():
  print(f"\n💰 Your current balance is: {balance} (Could be worse, right?)")


def deposit():
  global balance
  deposit_amount = float(input("\n📥 How much money do you want to bless your bank account with? "))
  balance += deposit_amount
  print(f"\n✅ Nice! Your wallet is slightly heavier now. New balance: {balance}")


def withdraw():
  global balance
  withdraw_amount = float(
      input("\n📤 How much money do you want to drain from your life savings? "))
  if withdraw_amount > balance:
    print("\n⚠️ Bro, you trying to withdraw air? You’re broke af! 💸💨")
  else:
    balance -= withdraw_amount
    print(  f"\n✅ Okay, hope you didn’t spend it on dumb stuff. New balance: {balance}" )


def exit_program():
  print("\n👋 Bye! Don't forget to check your balance before buying a Ferrari!")


# Main loop
print("🏦 Welcome to 'We Hope You Have Money' Bank!!")

while True:
  main()
  choice = input("\n🔢 Enter your choice (or just cry about your finances): ")

  if choice == "1":
    current_balance()
  elif choice == "2":
    deposit()
  elif choice == "3":
    withdraw()
  elif choice == "4":
    exit_program()
    break
  else:
    print("❌ Invalid choice! Even your decisions are broke. Try again.")
