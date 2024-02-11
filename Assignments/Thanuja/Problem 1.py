price = [100, 200, 300, 500, 250]
quantities = [5, 6, 10, 2, 3]

for i in range(5):
    print("Price and quantity for item", i + 1)
    print(" Price =", price[i])
    print(" Quantity =", quantities[i])
    print("Total Bill:")
    if quantities[i] > 5:
        print("Price after discount:")
        print((price[i] * quantities[i]) - (price[i] * 0.1 * quantities[i]))
    else:
        print(price[i] * quantities[i])
