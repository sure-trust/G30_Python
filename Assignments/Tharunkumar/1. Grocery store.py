def calculate_total_bill(prices, quantities):
    total = 0

    for price, quantity in zip(prices, quantities):
        item_total = price * quantity

        # Apply discount based on quantity
        if quantity >= 100:
            item_total *= 0.9  # 10% discount for quantities >= 100
        elif quantity >= 50:
            item_total *= 0.95  # 5% discount for quantities >= 50

        total += item_total

    return total

# Get input from the user
num_items = int(input("Enter the number of items: "))
prices = []
quantities = []

for i in range(num_items):
    price = float(input(f"Enter price for item {i + 1} Rs: "))
    quantity = int(input(f"Enter quantity for item {i + 1}: "))

    prices.append(price)
    quantities.append(quantity)

# Calculate and display the total bill
total_bill = calculate_total_bill(prices, quantities)
print(f"Total Bill: Rs:{total_bill:.2f}")
