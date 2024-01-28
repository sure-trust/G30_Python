assignment=float(input("Enter marks you have scored for assignment : "))
exams=float(input("Enter marks you have scored for exams:"))
attendance=float(input("Enter marks you have scored for attendance : "))
weight=assignment*0.20+exams*0.75+attendance*0.5
if weight<=60:
    grade='C'
elif weight>60 and weight<=80:
    grade='B'
else:
    grade='A'
print("Your total weight is = ",weight)
print("You have received grade = ",grade)
