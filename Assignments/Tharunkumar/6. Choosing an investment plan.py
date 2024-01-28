# Function-based Code for Investment Plan Comparison

def get_user_input():
    risk_tolerance = input("Enter your risk tolerance (low, medium, high): ")
    desired_returns = float(input("Enter your desired returns (%): "))
    return risk_tolerance, desired_returns

def compare_investment_options(risk_tolerance, desired_returns):
    if risk_tolerance == "low":
        if desired_returns < 5:
            return "Consider a savings account or low-risk bonds."
        elif 5 <= desired_returns < 10:
            return "Look into balanced funds or conservative portfolios."
        else:
            return "Explore moderate risk investments with a financial advisor."
    elif risk_tolerance == "medium":
        if desired_returns < 8:
            return "Explore a mix of stocks and bonds in a diversified portfolio."
        elif 8 <= desired_returns < 15:
            return "Consider a growth-focused mutual fund or ETF."
        else:
            return "Look into moderately aggressive investment options."
    elif risk_tolerance == "high":
        if desired_returns < 12:
            return "Consider a diverse portfolio with a higher allocation to stocks."
        elif 12 <= desired_returns < 20:
            return "Explore aggressive growth funds or individual stocks."
        else:
            return "Consult a financial professional for high-risk strategies."
    else:
        return "Invalid risk tolerance input. Please enter low, medium, or high."

# Main program
risk, returns = get_user_input()
result = compare_investment_options(risk, returns)
print(result)
