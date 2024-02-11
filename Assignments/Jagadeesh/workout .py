#Planning a workout routine? Design a program that suggests exercises based on fitness level and available equipment. 
#(Variables: fitness level, equipment; Operators: ==, !=; If-else: recommend exercises based on user's needs)

def suggest_exercises(fitness_level, equipment):
    beginner = {'bodyweight': ['push-ups', 'squats', 'lunges'],
                         'dumbbells': ['bicep curls', 'shoulder press', 'goblet squats']}

    intermediate = {'bodyweight': ['plank', 'burpees', 'mountain climbers'],
                              'dumbbells': ['deadlifts', 'rows', 'lateral raises']}

    advanced = {'bodyweight': ['pull-ups', 'plyometric push-ups', 'pistol squats'],
                          'dumbbells': ['snatch', 'overhead tricep extension', 'weighted step-ups']}

    if fitness_level == 'beginner':
        selected_exercises = beginner
    elif fitness_level == 'intermediate':
        selected_exercises = intermediate
    elif fitness_level == 'advanced':
        selected_exercises = advanced
    else:
        return "Invalid fitness level. Please choose beginner, intermediate, or advanced."

    available_exercises = selected_exercises.get(equipment, [])

    if not available_exercises:
        return "No suitable exercises found. Consider using a different type of equipment."

    else:
        return f"Consider including these exercises in your routine: {', '.join(available_exercises)}."

fitness_level = input("Enter your fitness level (beginner, intermediate, advanced): ")
equipment = input("Enter the equipment you have (bodyweight, dumbbells): ")

result = suggest_exercises(fitness_level, equipment)
print(result)