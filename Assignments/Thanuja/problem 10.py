schedule=int(input("Enter time in 24hrs format:(6-22)"))
medication=str(input("Enter medication type daily or weekly"))
if schedule<=12:
    if schedule<=6:
        if medication=="daily":
            print(" Reminder for Medication name A")
            dosage=2
        else:
            print("Reminder for Medication name B")
            dosage=1
    else:
        if medication=="daily":
            print(" Reminder for Medication name C")
            dosage=0.5
        else:
            print(" Reminder for Medication name D")
            dosage=1.5
else:
    if schedule<=17:
        if medication=="daily":
            print(" Reminder for Medication name E")
            dosage=3
        else:
            print("Reminder for Medication name F")
            dosage=1
    else:
        if medication=="daily":
            print(" Reminder for Medication name G")
            dosage=2.5
        else:
            print(" Reminder for Medication name H")
            dosage=0.5
print("Take dosage = ",dosage)