goal_amount = 10000
timeline_months = 12
current_savings = 2000
monthly_savings = (goal_amount - current_savings) / timeline_months
if monthly_savings > 0:
    print(f"You need to save ${monthly_savings:.2f} per month to reach your goal in {timeline_months} months.")
    if monthly_savings > 500:
        print("Consider increasing your income or reducing expenses to reach your goal.")
    else:
        print("You're on track! Keep up the good work!")
else:
    print("You've already saved enough to reach your goal!")