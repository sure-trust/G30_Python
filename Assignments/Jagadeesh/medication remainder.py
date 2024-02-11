#  10. Medication Reminder: Design a program that reminds patients to take their medication based on dosage and schedule, 
#considering potential interactions if taking multiple medications. (Variables: medication names, dosage, schedule; Operators: +, -, *, /; If-else: check for interactions based on medication types)


def remind_patient(medication_name, dosage, schedule):
    print(f"Reminder: Take {dosage} of {medication_name} at {schedule}")

def check_interactions(medication1, medication2):
    if medication1 == "Aspirin" and medication2 == "Ibuprofen":
        print("Warning: Potential interaction between Aspirin and Ibuprofen!")

medication_name1 = "Aspirin"
dosage1 = 1
schedule1 = "morning"

remind_patient(medication_name1, dosage1, schedule1)

medication_name2 = "Ibuprofen"
dosage2 = 2
schedule2 = "evening"

remind_patient(medication_name2, dosage2, schedule2)

check_interactions(medication_name1, medication_name2)

