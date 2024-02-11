def calculate_carbon_footprint(vehicles, energy_consumption, recycling_habits):
    # Calculate transportation footprint
    transportation_footprint = vehicles * 2500  # 2500 kg CO2 per vehicle per year

    # Calculate energy consumption footprint
    energy_footprint = energy_consumption * 0.5  # 0.5 kg CO2 per kWh consumed

    # Calculate recycling footprint
    recycling_footprint = 0
    if recycling_habits == "good":
        recycling_footprint = -500  # -500 kg CO2 per year if good recycling habits
    elif recycling_habits == "average":
        recycling_footprint = 0  # 0 kg CO2 per year if average recycling habits
    elif recycling_habits == "poor":
        recycling_footprint = 500  # 500 kg CO2 per year if poor recycling habits
    else:
        print("Invalid input for recycling habits. Please enter 'good', 'average', or 'poor'.")
        return None  # Return None in case of invalid input

    # Calculate total carbon footprint
    total_footprint = transportation_footprint + energy_footprint + recycling_footprint

    return total_footprint

# Get user inputs
vehicles = int(input("Enter the number of vehicles you have: "))
energy_consumption = float(input("Enter your annual energy consumption in kWh: "))
recycling_habits = input("Enter your recycling habits (good, average, or poor): ")

# Calculate and display carbon footprint
carbon_footprint = calculate_carbon_footprint(vehicles, energy_consumption, recycling_habits)

if carbon_footprint is not None:
    print("Your estimated carbon footprint is:", carbon_footprint, "kg CO2 per year")
