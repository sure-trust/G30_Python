price=float(input("enter the price of the product:"))
discount_percentage=float(input("enter the discount percentage:"))

if discount_percentage>=0 and discount_percentage<=100:
    discount_amount=(discount_percentage/100)*price
    discount_price=price-discount_amount
    print(f"the discount price is :{discount_price:.2f}")

else:
    print("invalid amount")   