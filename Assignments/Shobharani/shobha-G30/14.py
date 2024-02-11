def recycling_assistant():
    print("Welcome to the Recycling Assistant!")

    # Get user input for waste type
    waste_type = input("Enter the type of waste (e.g., plastic, paper, glass): ")

    # Match waste type to proper recycling or disposal methods
    if waste_type.lower() == 'plastic':
        disposal_method = "Recycle in designated plastic recycling bin."
    elif waste_type.lower() == 'paper':
        disposal_method = "Recycle in designated paper recycling bin."
    elif waste_type.lower() == 'glass':
        disposal_method = "Recycle in designated glass recycling bin."
    else:
        disposal_method = "Check local regulations for proper disposal instructions."

    # Display disposal method for the given waste type
    print(f"\nProper Disposal Method for {waste_type.capitalize()}:")
    print(disposal_method)

# Run the program
recycling_assistant()
