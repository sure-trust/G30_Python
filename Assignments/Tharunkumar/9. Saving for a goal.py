def calculate_progress(goal, timeline, current_savings):
    target_savings = goal / timeline
    savings_needed = target_savings * timeline
    progress = current_savings / savings_needed * 100

    return progress, target_savings, savings_needed

def suggest_adjustments(progress, target_savings):
    if progress >= 100:
        return "Congratulations! You've reached your savings goal!"
    else:
        shortfall = target_savings - progress
        if shortfall <= 0:
            return "You're on track. Keep it up!"
        else:
            return f"You need to save {shortfall:.2f} more to reach your goal on time."

# Get user input
goal_amount = float(input("Enter your savings goal amount: $"))
timeline_years = int(input("Enter your desired timeline (in years): "))
current_savings = float(input("Enter your current savings: $"))

# Calculate progress and suggest adjustments
progress, target_savings, savings_needed = calculate_progress(goal_amount, timeline_years, current_savings)
adjustment_message = suggest_adjustments(progress, target_savings)

# Display results
print(f"\nCurrent progress: {progress:.2f}%")
print(f"Target savings per year: ${target_savings:.2f}")
print(f"Total savings needed: ${savings_needed:.2f}")
print(adjustment_message)
