# Get input from the user
num_items = int(input("Enter the number of items: "))
prices = []
quantities = []

for i in range(num_items):
    price = float(input(f"Enter price for item {i + 1}: "))
    quantity = int(input(f"Enter quantity for item {i + 1}: "))

    prices.append(price)
    quantities.append(quantity)

# Calculate the total bill with discounts
total = 0

for price, quantity in zip(prices, quantities):
    item_total = price * quantity

    # Apply discount based on quantity
    if quantity >= 100:
        item_total *= 0.9  # 10% discount for quantities >= 100
    elif quantity >= 50:
        item_total *= 0.95  # 5% discount for quantities >= 50

    total += item_total

# Display the total bill
print(f"Total Bill: Rs:{total:.2f}")
