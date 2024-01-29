schedule=int(input("enter the time in 24 hours format(6-22)"))
medication=str(input("enter the medivation type daily or weekly"))

if schedule<=12:
    if medication=="daily":
        print("reminder for medication a")
        dosage=2
    else:
        print("reminder for medication b") 
        dosage=1
else:
    if medication=="daily":
        print("reminder for medication c")
        dosage=1
    else:
        print("reminder for medication d")
        dosage=2
print("take dosage=",dosage)