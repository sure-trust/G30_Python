
distance = float(input("enter the distance: "))
mileage = float(input("enter the mileage of vehicle: "))
gas_price = float(input("enter the gas price: "))
highway = float(input("enter the highway fuel efficiency : "))
city = float(input("enter the city fuel efficiency :"))
 
travel_time = distance/highway if distance>50 else distance /city
    
fuel_cost = (distance/mileage)*gas_price

print("enstimated travel time:  hours")
print(travel_time)
print("enstimated fuel cost:.f")
print(fuel_cost)

