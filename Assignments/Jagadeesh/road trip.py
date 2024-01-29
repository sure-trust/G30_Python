
#Planning a road trip? Write a program to estimate the travel time and fuel cost based on distance,
#vehicle mileage, and gas prices. (Variables: distance, mileage, gas price;
#Operators: *, /; If-else: consider different fuel efficiency for highway vs. city driving)

def road_trip(distance,gas_price,highway_mileage,city_mileage):
    speed = 65
    travel_time = distance / speed

    highway_fuel = distance / highway_mileage
    city_fuel = distance / city_mileage
 

    driving_condition = input("enter 'h' for highway or 'c' for city driving")
    if driving_condition.lower() == 'h':
        consumed_fuel = highway_fuel
    elif driving_condition.lower() == 'c':
        consumed_fuel = city_fuel
    else:
        print('invalid output')
    fuel_cost = consumed_fuel / gas_price
    return travel_time,fuel_cost

distance = float(input("Enter the miles: "))
highway_mileage = float(input("Enter the highway mileage: "))
city_mileage = float(input("Enter the city mileage: "))
gas_price = float(input("Enter the gas price: "))

travel_time, fuel_cost = road_trip(distance, highway_mileage, city_mileage, gas_price)

print(travel_time)
print(fuel_cost)