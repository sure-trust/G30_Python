# Code 1

# Get user input for grades
exam_grade = float(input("Enter exam percentage out of 100 : "))
assignment_grade = float(input("Enter assignment percentage out of 100 : "))
attendance_grade = float(input("Enter attendance percentage out of 100 : "))

# Define weights
exam_weight = 0.7
assignment_weight = 0.2
attendance_weight = 0.1

# Calculate final grade
final_grade = (exam_grade * exam_weight) + (assignment_grade * assignment_weight) + (attendance_grade * attendance_weight)

# Print the final grade
print(f"Your final grade is: {final_grade:.2f}")
