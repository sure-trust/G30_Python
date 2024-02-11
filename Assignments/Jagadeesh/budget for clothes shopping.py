#You have a budget for clothes shopping. Design a program to help you stay within your budget,
#considering item prices and offering suggestions if you go over. 
#(Variables: budget, item prices; Operators: -, <, >; If-else: check budget vs. total cost)

def budget_checker(budget, item_prices):
    total_amount = sum(item_prices)
    if total_amount <= budget:
        print(f'You are within your budget. Total cost: {total_amount}')
    else:
        overspend = total_amount - budget
        print(f'You have exceeded your budget by {overspend:}. plz remove your items')

budget = 10000
item_prices = [2000,4000,1000,5000]
budget_checker(budget, item_prices)
