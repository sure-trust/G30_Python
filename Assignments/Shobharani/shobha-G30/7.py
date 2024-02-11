
fitness_level = input("What is your fitness level? (beginner, intermediate, or advanced): ").lower()
equipment = input("What equipment do you have available? (none, dumbbells, resistance bands, or a gym): ").lower()


if fitness_level == "beginner":

    if equipment == "none":
        print("Here are some bodyweight exercises you can do at home:")
        print("- Squats")
        print("- Push-ups")
        print("- Lunges")
        print("- Plank")
        print("- Wall sits")


    elif equipment == "dumbbells":
        print("Here are some exercises you can do with dumbbells:")
        print("- Bicep curls")
        print("- Shoulder press")
        print("- Rows")
        print("- Glute bridges")
        print("- Dumbbell lunges")

else:
    print("Invalid fitness level. Please enter beginner, intermediate, or advanced")
