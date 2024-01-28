deadlines=float(input("Enter no of days left for submission:(1-5)"))
importance=int(input("Enter importance:"))
priority=deadlines*importance
if deadlines<=3:
    if deadlines<2:
        print("Task a with priority = ",priority)
    else:
        print("Task b with priority = ",priority)
else:
    if deadlines<=4:
        print("Task c with priority = ",priority)
    else:
        print("Task d with priority = ",priority)