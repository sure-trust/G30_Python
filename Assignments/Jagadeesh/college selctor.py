#College Major Selector: Design a program that helps students choose a college major based on their interests, skills, and job market trends. 
#(Variables: interests, skills, trends; Operators: ==, !=; If-else: match user profile to potential majors)

def college_major_selector(interests, skills, trends):

    stud_interests = input("Enter your interests (e.g., science, art, business): ").lower()
    stud_skills = input("Enter your skills (e.g., analytical, creative, communication): ").lower()
    job_market_trends = input("Consider the current job market trends? (yes/no): ").lower()

    if stud_interests == "science" and stud_skills == "analytical" and job_market_trends == "yes":
        print("Recommended Major: Computer Science or Data Science")
    elif stud_interests == "art" and stud_skills == "creative" and job_market_trends == "yes":
        print("Recommended Major: Graphic Design or Fine Arts")
    elif stud_interests == "business" and stud_skills == "communication" and job_market_trends == "yes":
        print("Recommended Major: Business Administration or Marketing")
    else:
        print("Unable to rstud_commend a specific major based on the provided information.")

college_major_selector("interests", "skills", "trends")

