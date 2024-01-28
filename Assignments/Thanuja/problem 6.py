risk=float(input("Enter a number such that user can take risk(2-5):"))
if risk<=3:
    if risk<3:
        print("Gold :")
        returns=5
    else:
        print("Stocks")
        returns=10
else:
    if risk<5:
        print("Real estate")
        returns=8
    else:
        print("Cryptocurrency")
        returns=15
print(returns)
