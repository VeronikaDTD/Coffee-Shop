

menu = {
    "Espresso": 3.00,
    "Latte": 4.50,
    "Cappuccino": 4.00,
    "Americano": 3.50,
    "Mocha": 5.00,
    "Tea": 2.50
}

order = []
total = 0

print("☕ Welcome to Fera Coffee Shop ☕")
print("\n---- MENU ----")

for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

while True:
    choice = input("\nEnter item name to order (or type 'done' to finish): ")

    if choice.lower() == "done":
        break

    if choice in menu:
        order.append(choice)
        total += menu[choice]
        print(f"{choice} added to your order.")
    else:
        print("Item not found. Please choose from the menu.")

print("\n---- ORDER SUMMARY ----")

if order:
    for item in order:
        print(f"- {item}: ${menu[item]:.2f}")

    print(f"\nTotal: ${total:.2f}")
    print("Thank you for visiting Python Coffee Shop! ☕")
else:
    print("No items ordered.")