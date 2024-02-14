#Grade Calculator: Build a program that calculates student grades based on assignments, exams, and attendance, 
#considering different weighting schemes for different factors. (Variables: grades, weights; Operators: +, -, *, /; If-else: apply different weights based on course policies)

def calculate_grade(assignments, exams, attendance):
    assignment = 1.2
    exam = 1.3
    attendance = 1.5

    weighted_sum = (assignments * assignment) + (exams * exam) + (attendance * attendance)

    if weighted_sum >= 90:
        grade = 'A'
    elif weighted_sum >= 80:
        grade = 'B'
    elif weighted_sum >= 70:
        grade = 'C'
    elif weighted_sum >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade

assignments_grade = float(input("Enter the assignments grade: "))
exams_grade = float(input("Enter the exams grade: "))
attendance_grade = float(input("Enter the attendance grade: "))
final_grade = calculate_grade(assignments_grade, exams_grade, attendance_grade)
print(final_grade)