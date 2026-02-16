# Concession Stand Program

menu = {
    "popcorn": 4.00, "soda": 2.00, "candy": 1.00, "chips": 3.00,
    "water": 1.00, "cookie": 2.00, "cake": 5.00, "pie": 3.00,
    "ice cream": 4.00, "chocolate": 2.00, "milk": 3.00, "juice": 2.00,
    "tea": 2.00, "coffee": 3.00, "hot chocolate": 4.00, "lemonade": 3.00,
}

cart = []
total = 0

print("--------------------------------")
print("Welcome to the Concession Stand!")
print("--------------------------------")
print("Menu:".center(30))
print("--------------------------------")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")
print("--------------------------------")

while True:
    food = input("\nSelect an item (q to quit): ").lower()

    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        total += menu[food]
        print(f"✅ Added {food} (${menu[food]:.2f}) to your cart.")
        print(f"🛒 Current Cart: {', '.join(cart)}")
        print(f"💰 Total: ${total:.2f}")
    else:
        print("❌ Item not found in the menu. Please try again.")

print("\n--------------------------------")
print("🛍️ Final Order Summary:")
if cart:
    for item in set(cart):
        print(f"{item.capitalize()} x {cart.count(item)} - ${menu[item] * cart.count(item):.2f}")
    print(f"\n💵 Grand Total: ${total:.2f}")
else:
    print("No items purchased.")
print("📌 Thank you for visiting the Concession Stand!")
