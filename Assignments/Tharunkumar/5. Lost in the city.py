# Function to recommend restaurants based on budget and preferences
def recommend_restaurants(budget, preferences):
    # Sample restaurant data (name, budget, cuisine)
    restaurants = [
        ("Restaurant A", 200, "Italian"),
        ("Restaurant B", 150, "Mexican"),
        ("Restaurant C", 300, "Asian"),
        ("Restaurant D", 250, "Vegetarian"),
        ("Restaurant E", 100, "Fast Food"),
    ]

    # Filter restaurants based on budget and preferences
    recommended_restaurants = []
    for name, restaurant_budget, cuisine in restaurants:
        if restaurant_budget <= budget:
            if preferences == "Vegetarian" and cuisine == "Vegetarian":
                recommended_restaurants.append(name)
            elif preferences == "Non-Vegetarian" and cuisine != "Vegetarian":
                recommended_restaurants.append(name)
            elif preferences == "Any":
                recommended_restaurants.append(name)

    return recommended_restaurants

# User input
user_budget = int(input("Enter your budget (100 - 200) Rs: "))
user_preferences = input("Enter your dietary preferences (Vegetarian/Non-Vegetarian/Any): ")

# Recommend restaurants
recommended_list = recommend_restaurants(user_budget, user_preferences)

# Display recommendations
if recommended_list:
    print("Recommended restaurants:")
    for restaurant in recommended_list:
        print(restaurant)
else:
    print("No restaurants found that match your criteria.")
