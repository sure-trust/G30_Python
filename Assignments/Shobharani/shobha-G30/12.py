
courses = {
    "Math": {
        "assignments": [75, 80, 90],
        "exams": [85, 95],
        "attendance": 90,
        "weights": {"assignments": 0.4, "exams": 0.5, "attendance": 0.1}
    },
    "English": {
        "assignments": [88, 92, 85],
        "exams": [98],
        "attendance": 85,
        "weights": {"assignments": 0.3, "exams": 0.6, "attendance": 0.1}
    }
}

for course_name, course_data in courses.items():
    assignments_avg = sum(course_data["assignments"]) / len(course_data["assignments"])
    exams_avg = sum(course_data["exams"]) / len(course_data["exams"])
    weighted_average = (assignments_avg * course_data["weights"]["assignments"] +
                       exams_avg * course_data["weights"]["exams"] +
                       course_data["attendance"] * course_data["weights"]["attendance"])
    print(f"{course_name} grade: {weighted_average:.2f}")
