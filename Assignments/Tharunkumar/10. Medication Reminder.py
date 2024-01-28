# Medication reminder program using for loop and basic if-else statements

num_medications = int(input("Enter the number of medications: "))

for i in range(num_medications):
    medication_name = input(f"Enter the name of Medication {i + 1}: ")
    dosage = float(input(f"Enter the dosage for {medication_name} (in mg): "))
    schedule = input(f"Enter the schedule for {medication_name} (e.g., 'morning', 'afternoon', 'evening'): ")

    print(f"\nReminder for {medication_name}:")

    if schedule.lower() == 'morning':
        print(f"Take {dosage} mg in the morning.")
    elif schedule.lower() == 'afternoon':
        print(f"Take {dosage} mg in the afternoon.")
    elif schedule.lower() == 'evening':
        print(f"Take {dosage} mg in the evening.")
    else:
        print("Invalid schedule provided. Please enter 'morning', 'afternoon', or 'evening'.")
