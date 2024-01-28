import datetime

# Store medication information
medications = {}

# Add a medication
def add_medication(name, dosage, schedule):
    medications[name] = {"dosage": dosage, "schedule": schedule, "last_taken": None}

# Generate reminders based on schedule
def generate_reminders():
    now = datetime.datetime.now()  # Get current time
    for name, data in medications.items():
        if data["schedule"] == "daily":
            if data["last_taken"] is None or (now - data["last_taken"]).days >= 1:
                print(f"Take {data['dosage']} of {name}.")
                data["last_taken"] = now

# Example usage
add_medication("Aspirin", "1 tablet", "daily")
add_medication("Ibuprofen", "2 tablets", "every 4 hours")

generate_reminders()
