def suggest_camping_gear_weather(weather, amenities):
    if weather == "sunny":
        if amenities == "basic":
            return "Pack a tent, sleeping bag, and basic cooking equipment."
        elif amenities == "luxury":
            return "Bring a comfortable tent, sleeping bag, and a full set of cooking gear. Don't forget some leisure items like a portable chair and a book."
        else:
            return "Invalid amenities input."

    elif weather == "rainy":
        if amenities == "basic":
            return "Include a waterproof tent, rainfly, and waterproof clothing. Consider a waterproof ground tarp."
        elif amenities == "luxury":
            return "Pack a high-quality waterproof tent, rainfly, waterproof clothing, and a waterproof backpack. Bring a portable canopy for extra shelter."
        else:
            return "Invalid amenities input."

    else:
        return "Invalid weather input."

# Get user input
user_weather = input("Enter the weather conditions (sunny/rainy): ").lower()
user_amenities = input("Enter the campsite amenities (basic/luxury): ").lower()

# Call the function and display the suggestion
gear_suggestion = suggest_camping_gear_weather(user_weather, user_amenities)
print("Gear Suggestion:", gear_suggestion)
