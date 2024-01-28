def calculate_travel_time_and_fuel_cost(distance, mileage, gas_price, driving_type):
    if driving_type.lower() == 'highway':
        efficiency = 1.2  # Adjust for highway driving efficiency
    else:
        efficiency = 1.0  # Default for city driving

    travel_time = distance / 60  # Assuming an average speed of 60 mph
    fuel_cost = (distance / mileage) * gas_price * efficiency

    return travel_time, fuel_cost

# Get user input
distance = float(input("Enter the distance of the road trip in Km : "))
mileage = float(input("Enter your vehicle's mileage in Km  per litter : "))
gas_price = float(input("Enter the current gas/petrol/diesel price per litter Rs: "))
driving_type = input("Enter 'highway' or 'city' for driving type: ")

# Calculate and display results
time, cost = calculate_travel_time_and_fuel_cost(distance, mileage, gas_price, driving_type)
print(f"Estimated travel time: {time:.2f} hours")
print(f"Estimated fuel cost Rs: {cost:.2f}")
