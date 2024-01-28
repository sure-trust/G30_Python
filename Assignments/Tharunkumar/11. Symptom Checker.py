def symptom_checker_1():
    symptoms = ["fever", "cough", "headache", "fatigue", "shortness of breath"]

    user_symptoms = []
    for symptom in symptoms:
        response = input(f"Do you have {symptom}? (yes/no): ").lower()
        if response == "yes":
            user_symptoms.append(symptom)

    if not user_symptoms:
        print("No symptoms reported. You may be healthy.")
    else:
        print("You have the following symptoms:", user_symptoms)

        # Matching symptoms to possible causes
        if "fever" in user_symptoms and "shortness of breath" in user_symptoms:
            print("Possible cause: COVID-19. Seek medical attention.")
        elif "fever" in user_symptoms or "cough" in user_symptoms:
            print("Possible cause: Flu or common cold. Rest at home and drink fluids.")
        elif "headache" in user_symptoms:
            print("Possible cause: Stress or tension. Take a break and relax.")
        else:
            print("No specific cause identified. Monitor your symptoms.")


symptom_checker_1()
