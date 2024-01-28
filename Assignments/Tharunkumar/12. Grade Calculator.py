# Code 2

# Get user input for grades
exam_grade = float(input("Enter overall exam percentage out of 100 : "))
assignment_grade = float(input("Enter overall assignment percentage out of 100 : "))
attendance_grade = float(input("Enter overall attendance percentage out of 100 : "))

# Define weights
exam_weight = 0.7
assignment_weight = 0.2
attendance_weight = 0.1

# Check if grades are within the valid range (0-100)
if 0 <= exam_grade <= 100 and 0 <= assignment_grade <= 100 and 0 <= attendance_grade <= 100:
    # Calculate final grade based on weights
    if exam_grade >= 0 and assignment_grade >= 0 and attendance_grade >= 0:
        final_grade = (exam_grade * exam_weight) + (assignment_grade * assignment_weight) + (attendance_grade * attendance_weight)
        # Print the final grade
        print(f"Your final grade is: {final_grade:.2f}")
    else:
        print("Grades cannot be negative. Please enter valid grades.")
else:
    print("Invalid input. Grades should be between 0 and 100.")
