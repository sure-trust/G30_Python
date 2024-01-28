
symptoms_causes = {
    "fever": ["flu", "common cold", "COVID-19", "infection"],
    "cough": ["flu", "common cold", "COVID-19", "allergies"],
    "headache": ["flu", "common cold", "migraine", "stress"],

}


symptoms = []
while True:
    symptom = input("Enter a symptom (or 'done' to finish): ").lower()
    if symptom == "done":
        break
    symptoms.append(symptom)


possible_causes = set()
for symptom in symptoms:
    possible_causes.update(symptoms_causes[symptom])


print("Possible causes of your symptoms:")
for cause in possible_causes:
    print(f"- {cause}")

print("\nRemember, this is not a substitute for professional medical advice. If you are concerned about your symptoms, please consult a doctor.")

