# Basic Code for Investment Plan Comparison

# Get user input
risk_tolerance = input("Enter your risk tolerance (low, medium, high): ")
desired_returns = float(input("Enter your desired returns (%): "))

# Compare investment options based on user input
if risk_tolerance == "low":
    if desired_returns < 5:
        print("Consider a savings account or low-risk bonds.")
    elif 5 <= desired_returns < 10:
        print("Look into balanced funds or conservative portfolios.")
    else:
        print("Explore moderate risk investments with a financial advisor.")
elif risk_tolerance == "medium":
    if desired_returns < 8:
        print("Explore a mix of stocks and bonds in a diversified portfolio.")
    elif 8 <= desired_returns < 15:
        print("Consider a growth-focused mutual fund or ETF.")
    else:
        print("Look into moderately aggressive investment options.")
elif risk_tolerance == "high":
    if desired_returns < 12:
        print("Consider a diverse portfolio with a higher allocation to stocks.")
    elif 12 <= desired_returns < 20:
        print("Explore aggressive growth funds or individual stocks.")
    else:
        print("Consult a financial professional for high-risk strategies.")
else:
    print("Invalid risk tolerance input. Please enter low, medium, or high.")
