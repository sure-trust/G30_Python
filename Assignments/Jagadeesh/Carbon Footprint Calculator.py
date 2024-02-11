#Carbon Footprint Calculator: Create a program that estimates an individual's carbon footprint based on their transportation, energy usage, and consumption habits. 
#(Variables: activities, consumption; Operators: +, -, *, /; If-else: calculate footprint based on different factors)
#Recycling Assistant: Design a program that identifies different types of waste and suggests proper recycling
#or disposal methods based on local regulations. (Variables: waste type; Operators: ==, !=; If-else: match waste to disposal methods)

def carbon_footprint_calculator(transportation, energy_usage, consumption):

    transportation_emission = float(input("Enter your annual transportation emissions (in metric tons of CO2): "))
    energy_usage_emission = float(input("Enter your annual energy usage emissions (in metric tons of CO2): "))
    consumption_emission = float(input("Enter your annual consumption emissions (in metric tons of CO2): "))

    total_carbon_footprint = transportation_emission + energy_usage_emission + consumption_emission

    if total_carbon_footprint <= 5:
        print("Your carbon footprint is relatively low. Keep up the good work!")
    elif 5 < total_carbon_footprint <= 10:
        print("Your carbon footprint is moderate. Consider making some eco-friendly changes.")
    else:
        print("Your carbon footprint is high. Explore ways to reduce your environmental impact.")

carbon_footprint_calculator("transportation", "energy_usage", "consumption")

#Recycling assist

def recycling_assistant(waste_type):

    waste_type = input("Enter the type of waste (e.g., plastic, paper, glass): ").lower()
    if waste_type == "plastic":
        print("Recycling Method: Check local recycling guidelines. Dispose of plastic in the recycling bin if accepted.")
    elif waste_type == "paper":
        print("Recycling Method: Most paper is recyclable. Place it in the recycling bin.")
    elif waste_type == "glass":
        print("Recycling Method: Glass is recyclable. Put it in the recycling bin, but check local guidelines.")
    else:
        print("Disposal Method: Check local regulations for proper disposal of this type of waste.")
recycling_assistant("waste_type")
