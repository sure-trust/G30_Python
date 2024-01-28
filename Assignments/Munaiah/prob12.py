assignment=float(input("Enter marks you have scored for assignment : "))
exams=float(input("Enter marks you have scored for exams:"))
attendance=float(input("Enter marks you have scored for attendance : "))
weight=assignment*0.4+exams*0.5+attendance*0.1
if weight>=90:
    grade='A'
elif weight>=80:
    grade='B'
elif weight>=70:
    grade='C'
else:
    grade="F"
print("Your total weight is = ",weight)
print("You have received grade = ",grade)