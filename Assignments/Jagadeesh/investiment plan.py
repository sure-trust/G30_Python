#Choosing an investment plan? Build a program that compares different investment options based on risk tolerance and desired returns.
# (Variables: risk tolerance, returns; Operators: +, -, *, /; If-else: suggest options based on user's profile).

def investment_plan(risk_tolerance, returns):
    conservative_portfolio = "Bonds and low-risk assets"
    balanced_portfolio = "Mix of stocks and bonds"
    aggressive_portfolio = "Stocks and high-risk assets"

    if risk_tolerance == "low":
        if returns < 5:
            return conservative_portfolio
        elif returns >= 5 and returns < 10:
            return balanced_portfolio
        else:
            return aggressive_portfolio
    elif risk_tolerance == "medium":1
        if returns < 8:
            return balanced_portfolio
        elif returns >= 8 and returns < 12:
            return aggressive_portfolio
        else:
            return "Consider professional advice for high-risk options"
    elif risk_tolerance == "high":
        if returns < 10:
            return aggressive_portfolio
        else:
            return "Consider professional advice for high-risk options"
    else:
        return "Invalid risk tolerance level"

risk_tolerance = input("Enter your risk tolerance (low, medium, high): ")
returns = float(input("Enter your returns: "))
result = investment_plan(risk_tolerance, returns)
print(result)