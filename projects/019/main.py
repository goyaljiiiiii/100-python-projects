# Defining menu of my cafe
menu = {
    "Coffee": 2.50,
    "Tea": 1.75,
    "Espresso": 3.00,
    "Cappuccino": 3.50,
    "Latte": 3.75,
    "Hot Chocolate": 2.75,
    "Muffin": 2.00,
    "Bagel": 1.50,
    "Sandwich": 5.00,
    "Smoothie": 4.25,
    "Iced Coffee": 3.00,
    "Iced Tea": 2.00,
    "Brownie": 2.50,
    "Cookie": 1.75,
    "Granola Bar": 1.50,
}

print("Welcome to \"MY CAFE\". Umm..not yours, it's mine actually 😎")

# Print the menu items and their prices
print("\nNow, look at the menu and also the prices... it's not a bargain sale, but it's good!")
for item, price in menu.items():
    print(f"{item}: ₹{price:.2f}")


def order():
    order_list = []
    order_bill = 0
    while True:
        item_order = input("What do you want to order? (Type 'done' when finished): ")
        item_order_format = item_order.title()
        if item_order.lower() == "done":
            break
        if item_order_format in menu:
            order_list.append(item_order_format)
            order_bill += menu[item_order_format]
            print(f"🍽️ Your current order: {item_order_format}, Total bill: ₹{order_bill:.2f}")
        else:
            print("❌ Sorry, we don't have that. Try again!")

    if order_list:
        print("\n🧾 **Your final order:**", ", ".join(order_list))
        print(f"💰 Total Bill: ₹{order_bill:.2f}")
    else:
        print("👀 You ordered nothing... Are you sure you're not hungry?")


order()
