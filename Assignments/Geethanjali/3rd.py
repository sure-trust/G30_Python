distance=int(input("enter distance in miles:"))
gas_price=int(input("enter gas price:"))
way=str(input("enter way like highway or city:"))
if(way=="highway"):
    mileage=25
else:
    mileage=30
    fuel_cost=(distance/mileage)*gas_price
    travel_time=(distance*1.6)*20
    print("fuel cost=",fuel_cost,"travel time in min=",travel_time)
