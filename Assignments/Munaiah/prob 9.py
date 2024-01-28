goal_amount=float(input("Enter amount:"))
timeline=int(input("Enter time left in months:"))
current_savings=float(input("Enter amount saved:"))
if current_savings  - goal_amount >=0:
    print("You have enough amount")
else :
    print("Amount to be earned ", goal_amount - current_savings  ,"time left = ",timeline)

