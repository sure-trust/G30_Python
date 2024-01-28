def major_selector():
    print("Welcome to the College Major Selector!")

    # Get user input for interests, skills, and preferences
    interests = input("Enter your interests (e.g., science, art, business): ")
    skills = input("Enter your skills (e.g., analytical, creative, communication): ")

    # Get user preference for job market trends
    job_market_trends_preference = input("Are you interested in majors with high job market demand? (yes/no): ")

    # Predefined criteria for potential majors
    science_majors = ['Physics', 'Biology', 'Computer Science']
    art_majors = ['Fine Arts', 'Graphic Design', 'Film Studies']
    business_majors = ['Marketing', 'Finance', 'Entrepreneurship']

    # Match user profile to potential majors
    if interests.lower() == 'science' and skills.lower() == 'analytical':
        recommended_majors = science_majors
    elif interests.lower() == 'art' and skills.lower() == 'creative':
        recommended_majors = art_majors
    elif interests.lower() == 'business' and skills.lower() == 'communication':
        recommended_majors = business_majors
    else:
        recommended_majors = ["Undecided"]

    # Consider job market trends preference
    if job_market_trends_preference.lower() == 'yes':
        recommended_majors = [major + " (High Demand)" for major in recommended_majors]

    # Display recommended majors
    print("\nRecommended Majors:")
    for major in recommended_majors:
        print(f"- {major}")


# Run the program
major_selector()

