#Saving for a goal? Build a program that tracks your progress and suggests adjustments to your saving plan based on your desired timeline. 
#(Variables: goal amount, timeline, current savings; Operators: +, -, *, /; If-else: suggest changes based on progress).

def track_progress(goal_amount, timeline, current_savings):
    progress_percentage = (current_savings / goal_amount) * 100

    if progress_percentage >= 100:
        print("Congratulations! You've reached your savings goal.")
    else:
        remaining_timeline = timeline - 1  
        remaining_savings_needed = goal_amount - current_savings
        required_monthly_savings = remaining_savings_needed / remaining_timeline

        if required_monthly_savings > 0:
            print(f"You are on track with {progress_percentage:} progress.")
            print(f"To reach your goal on time, consider saving approximately {required_monthly_savings:} per month.")
        else:
            print("You've exceeded your savings goal! Adjust your timeline or set a new goal.")

goal_amount = 10000
timeline = 12  
current_savings = 5000

track_progress(goal_amount, timeline, current_savings)
