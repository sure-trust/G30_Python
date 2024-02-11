def symptom_checker_if_elif():
    print("Welcome to the Symptom Checker!")
    symptoms = input("Please enter your symptoms (comma-separated): ").lower().split(',')

    if 'fever' in symptoms:
        print("You may have a common fever. Rest and take over-the-counter medications as needed.")
    elif 'cough' in symptoms:
        print("You may have a cold or flu. Rest and stay hydrated. If symptoms persist, consult a doctor.")
    elif 'shortness of breath' in symptoms:
        print("Seek medical attention immediately. Shortness of breath may indicate a serious condition.")
    elif 'headache' in symptoms:
        print("You may be experiencing a headache. Ensure you are well-hydrated and consider taking pain relievers.")
    else:
        print("We couldn't identify the specific cause of your symptoms. Consult a doctor for a proper diagnosis.")

symptom_checker_if_elif()
