def suggest_workout_advanced(fitness_level, has_equipment):
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
    elif fitness_level == 'intermediate':
        if has_equipment:
            print("Great choice! Here's an intermediate workout plan with equipment:")
            print("1. Barbell Squats: 4 sets of 10 reps")
            print("2. Bench Press: 4 sets of 8 reps")
            print("3. Pull-ups: 3 sets to failure")
        else:
            print("Nice! Here's an intermediate workout plan without equipment:")
            print("1. Jumping Lunges: 4 sets of 12 reps")
            print("2. Tricep Dips: 3 sets of 15 reps")
            print("3. Plank with Shoulder Taps: 3 sets of 45 seconds")
    else:
        print("Please choose a valid fitness level: beginner or intermediate")

# Get user input
fitness_level_input = input("Enter your fitness level (beginner/intermediate): ").lower()
equipment_input = input("Do you have equipment? (yes/no): ").lower()

# Validate input and suggest workout
if fitness_level_input == 'beginner' or fitness_level_input == 'intermediate':
    if equipment_input == 'yes' or equipment_input == 'no':
        suggest_workout_advanced(fitness_level_input, equipment_input)
    else:
        print("Invalid equipment input. Please enter 'yes' or 'no'.")
else:
    print("Invalid fitness level. Please enter 'beginner' or 'intermediate'.")
