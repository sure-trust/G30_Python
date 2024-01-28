# Code 1

# List of available majors with corresponding interests and skills
majors_data = {
    'Computer Science': {'interests': ['programming', 'problem-solving'], 'skills': ['coding', 'algorithms']},
    'Business Administration': {'interests': ['leadership', 'management'], 'skills': ['communication', 'strategic planning']},
    'Psychology': {'interests': ['human behavior', 'empathy'], 'skills': ['listening', 'analytical thinking']}
    # Add more majors as needed
}
print("""Here are the list of curses and their corresponding interest and skills
Computer Science                                Business Administration                         Psychology
    interests : programming,problem-solving         interests : leadership,management               interests : human behavior,empathy
    skills : coding,algorithms                      skills : communication,strategic planning       skills : listening,analytical thinking
""")
# Get user input for interests and skills
user_interests = input("Enter your interests (comma-separated): ").split(',')
user_skills = input("Enter your skills (comma-separated): ").split(',')

# Match user profile to potential majors
matched_majors = []

for major, data in majors_data.items():
    if set(user_interests) == set(data['interests']) and set(user_skills) == set(data['skills']):
        matched_majors.append(major)

# Display the matched majors
if matched_majors:
    print("Potential majors for you: ", ', '.join(matched_majors))
else:
    print("No matching majors found. Consider exploring more options.")
