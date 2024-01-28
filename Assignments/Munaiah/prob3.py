distance=int(input("Enter distance in miles:"))
gas_price=int(input("Enter gas price:"))
way=str(input("enter way like highway or city:"))
if way=="highway":
    mileage=35
else:
    mileage=50
fuel_cost=(distance/mileage)*gas_price
travel_time=(distance*1.8)*20
print("Fuel Cost=",fuel_cost,"Travel Time in mins =",travel_time)
