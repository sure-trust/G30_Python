def suggest_workout_basic(fitness_level, has_equipment):
    if fitness_level == 'beginner':
        if has_equipment:
            print("Great choice! Here's a basic workout plan for beginners with equipment:")
            print("1. Bodyweight Squats: 3 sets of 12 reps")
            print("2. Push-ups: 3 sets of 10 reps")
            print("3. Bent-over Rows: 3 sets of 12 reps")
        else:
            print("Awesome! Here's a basic workout plan for beginners without equipment:")
            print("1. Bodyweight Squats: 3 sets of 12 reps")
            print("2. Push-ups: 3 sets of 10 reps")
            print("3. Plank: 3 sets of 30 seconds")
    else:
        print("Please choose a valid fitness level: beginner")

# Get user input
fitness_level_input = input("Enter your fitness level (beginner): ").lower()
equipment_input = input("Do you have equipment? (yes/no): ").lower()

# Validate input and suggest workout
if fitness_level_input == 'beginner':
    if equipment_input == 'yes' or equipment_input == 'no':
        suggest_workout_basic(fitness_level_input, equipment_input)
    else:
        print("Invalid equipment input. Please enter 'yes' or 'no'.")
else:
    print("Invalid fitness level. Please enter 'beginner'.")

