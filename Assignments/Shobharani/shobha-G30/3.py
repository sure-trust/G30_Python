distance = float(input("Enter the distance : "))
mileage = float(input("Enter your vehicle's mileage: "))
gas_price = float(input("Enter the current gas price:"))
driving_type = input("Is this primarily highway or city driving? (Enter 'highway' or 'city'): ")
if driving_type.lower() == "city":
    mileage = mileage * 0.8
fuel_needed = distance / mileage
fuel_cost = fuel_needed * gas_price
travel_time = distance / 60
print("Estimated fuel cost:", round(fuel_cost, 2))
print("Estimated travel time:", round(travel_time, 2), "hours")
