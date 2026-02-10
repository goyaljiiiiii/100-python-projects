print("Project 015 - Restaurant Order")
foods = ["pizza", "burger", "fries", "chicken", "chips"]
prices = [2.00, 3.00, 1.50, 4.00, 1.00]
user_order = []
total = 0

print("Welcome to the restaurant!")
print("Here is the menu:")
for i in range(len(foods)):
  print(f'{foods[i]}={prices[i]}')

while True:
  food = input("Enter a food to buy(q to quit):")
  if food.lower() == "q":
    break
  else:
    user_order.append(food)
    total = total + float(prices[foods.index(food)])
    print(f'You have ordered {food} and total is {total}')
