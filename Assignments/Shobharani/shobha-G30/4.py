weather = input("What is the expected weather? (sunny, rainy, cold): ")
amenities = input("amenities are available at the campsite? (water, showers, firewood, none): ")
if weather == "sunny":
    print("Pack sunscreen, sunglasses, a hat, and light, breathable clothing.")
elif weather == "rainy":
    print("Pack rain gear (jacket, pants, boots), a tarp, and extra towels.")
elif weather == "cold":
    print("Pack warm clothes, a sleeping bag rated for cold temperatures, and a heater if allowed.")
else:
    print("Invalid weather input. Please try again.")
if "water" not in amenities.lower():
    print("Pack plenty of drinking water and water for cooking.")
if "showers" not in amenities.lower():
    print("Pack toiletries for bathing and personal hygiene.")
if "firewood" not in amenities.lower():
    print("Pack firewood if you plan to have a campfire.")
