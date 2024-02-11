risk_tolerance = input("what you choose in risk:(low,high,moderate)")
desired_returns = input("what you choose in returns:(low,high,moderate)")
if risk_tolerance == "low":
    if desired_returns == "low":
        print("Suggest low-risk options like bonds and money market funds.")
    else:
        print("Consider balanced funds or income-oriented equity funds.")
elif risk_tolerance == "moderate":
    if desired_returns == "low":
        print("Balanced funds or income-oriented equity funds might be suitable.")
    else:
        print("Growth-oriented equity funds or dividend-paying stocks could be options.")
else:
    if desired_returns == "low":
        print("Growth-oriented equity funds or dividend-paying stocks might be suitable with careful selection.")
    else:
        print("Aggressive growth funds or individual stock picking could be considered, but with high risk.")