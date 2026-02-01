inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# Print Inventory
print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {quantity}")

print()  

# Categories Set
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics.union(accessories)
print(f"All product categories: {all_products}")

print()  

price_list = []
for (price, quantity) in inventory.values():
    price_list.append(price)

print(f"Price list: {price_list}")

sorted_prices = sorted(price_list)
print(f"Sorted prices: {sorted_prices}")
print(f"Lowest price: ${sorted_prices[0]:.2f}")
print(f"Highest price: ${sorted_prices[-1]:.2f}")

print()  

inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {quantity}")
