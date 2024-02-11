def calculate_total_cost():
    total_cost = 0
    for i in range(1, 6):
        item_price = float(input(f"Enter the price of Travel Adventure {i} Rs:"))
        total_cost += item_price

    return total_cost


def check_budget(budget, total_spent):
    if total_spent > budget:
        print("Warning: You have exceeded your budget!")
        print(f"Total spent Rs:{total_spent}, Budget Rs:{budget}")
        overspent_amount = total_spent - budget
        print(f"You overspent by Rs:{overspent_amount}. Consider adjusting your choices.")

    else:
        remaining_budget = budget - total_spent
        print(f"Congratulations! You stayed within your budget.")
        print(f"Remaining budget Rs:{remaining_budget}")


def main():
    user_budget = float(input("Enter your budget Rs:"))
    total_spent = calculate_total_cost()
    check_budget(user_budget, total_spent)


if __name__ == "__main__":
    main()
