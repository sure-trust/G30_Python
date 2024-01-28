risk=float(input("Enter a number such that user can take risk(2-5):"))
if risk<=2:
    if risk<2:
        print("Gold :")
        returns=8
    else:
        print("Stocks")
        returns=20
else:
    if risk<3:
        print("Real estate")
        returns=8
    else:
        print("Cryptocurrency")
        returns=15
print(returns)