budget = int(input("Enter budget of yours "))
item_prices = [200, 500, 450, 1000]
sum_items = 0

for price in item_prices:
    sum_items += price

print("Sum of items:", sum_items)

if sum_items <= budget:
    print("Remaining amount =", budget - sum_items)
else:
    shortfall = sum_items - budget
    print("Insufficient amount to purchase:", shortfall)
    sum_without_item = 0

    for price in item_prices:
        if shortfall <= price:
            sum_without_item = sum_items - price
            break

print("After removing the item:", sum_without_item)
