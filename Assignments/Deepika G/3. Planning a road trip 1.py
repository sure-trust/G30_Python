# Get user input
distance = float(input("Enter the distance of the road trip in Km: "))
mileage = float(input("Enter your vehicle's mileage in Km per litter: "))
gas_price = float(input("Enter the current gas/petrol/diesel price per litter: "))
driving_type = input("Enter 'highway' or 'city' for driving type: ")

# Adjust efficiency based on driving type
if driving_type.lower() == 'highway':
    efficiency = 1.2  # Adjust for highway driving efficiency
else:
    efficiency = 1.0  # Default for city driving

# Calculate travel time and fuel cost
travel_time = distance / 60  # Assuming an average speed of 60 mph
fuel_cost = (distance / mileage) * gas_price * efficiency

# Display results
print(f"Estimated travel time: {travel_time:.2f} hours")
print(f"Estimated fuel cost Rs:{fuel_cost:.2f}")
