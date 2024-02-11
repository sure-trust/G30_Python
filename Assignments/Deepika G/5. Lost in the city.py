# Function to recommend restaurants based on budget and preferences
def recommend_restaurants(budget, preferences):
    # Sample restaurant data (name, budget, cuisine)
    restaurants = [
        {"name": "Restaurant A", "budget": 20, "cuisine": "Italian"},
        {"name": "Restaurant B", "budget": 15, "cuisine": "Mexican"},
        {"name": "Restaurant C", "budget": 30, "cuisine": "Asian"},
        {"name": "Restaurant D", "budget": 25, "cuisine": "Vegetarian"},
        {"name": "Restaurant E", "budget": 10, "cuisine": "Fast Food"},
    ]

    # Filter restaurants based on budget and preferences
    recommended_restaurants = []
    for restaurant in restaurants:
        if restaurant["budget"] <= budget:
            if preferences == "Vegetarian" and restaurant["cuisine"] == "Vegetarian":
                recommended_restaurants.append(restaurant["name"])
            elif preferences == "Non-Vegetarian" and restaurant["cuisine"] != "Vegetarian":
                recommended_restaurants.append(restaurant["name"])
            elif preferences == "Any":
                recommended_restaurants.append(restaurant["name"])

    return recommended_restaurants

# User input
user_budget = int(input("Enter your budget Rs: "))
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
