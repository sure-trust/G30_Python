#Symptom Checker: Create a program that asks users about their symptoms and suggests possible causes based on a knowledge base,
# recommending when to seek medical attention. (Variables: symptoms; Operators: ==, !=; If-else: match symptoms to possible causes)

def symptom_checker():
    symptom1 = input("fever? (yes/no): ").lower()
    symptom2 = input("coughing? (yes/no): ").lower()
    symptom3 = input(" body aches? (yes/no): ").lower()

    if symptom1 == "yes" and symptom2 == "yes" and symptom3 == "yes":
        print("Possible cause: Flu")
        print("Recommendation: Rest, stay hydrated, and consider over-the-counter flu medications.")
        print("If symptoms persist or worsen, consult a healthcare professional.")
    elif symptom1 == "yes" and symptom2 == "yes" and symptom3 == "no":
        print("Possible cause: Common cold")
        print("Recommendation: Rest, stay hydrated, and consider over-the-counter cold medications.")
        print("If symptoms persist or worsen, consult a healthcare professional.")
    elif symptom1 == "no" and symptom2 == "yes" and symptom3 == "yes":
        print("Possible cause: Muscle strain or injury")
        print("Recommendation: Rest, apply ice or heat, and consider over-the-counter pain relievers.")
        print("If symptoms persist or worsen, consult a healthcare professional.")
    else:
        print("Unable to determine possible causes based on provided symptoms.")
        print("It's recommended to consult a healthcare professional for a more accurate diagnosis.")

symptom_checker()

