def suggest_camping_gear_detailed(weather, amenities):
    if weather == "sunny":
        print("Pack sunscreen, a hat, sunglasses, lightweight clothing, and a reusable water bottle.")
    elif weather == "rainy":
        print("Bring a waterproof jacket, rain boots, a rain cover for your tent, and a pack of waterproof matches.")
    elif weather == "cold":
        print("Pack thermal layers, a warm jacket, gloves, a beanie, and a thermos with hot drinks.")
    else:
        print("Check the weather conditions and pack accordingly.")

    if amenities == "fire pit":
        print("Consider bringing marshmallows, skewers, and firewood for a cozy campfire.")
    elif amenities == "electricity":
        print("Bring electronic devices, chargers, and a power strip for convenience.")
    else:
        print("Check the campsite amenities and pack accordingly.")

# Get user input
user_weather = input("Enter the weather conditions (sunny, rainy, cold): ").lower()
user_amenities = input("Enter campsite amenities (fire pit, electricity): ").lower()

# Call the function
suggest_camping_gear_detailed(user_weather, user_amenities)
