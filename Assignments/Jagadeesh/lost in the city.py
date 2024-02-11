def recommend_restaurants(budget, preferences):
    restaurants = [
        {"name": "kfc", "cuisine": "Italian", "budget": "Moderate", "vegetarian": False},
        {"name": "mcdonalds", "cuisine": "Mexican", "budget": "Affordable", "vegetarian": True},
        {"name": "bbq", "cuisine": "Asian", "budget": "Expensive", "vegetarian": True},
        {"name": "noma", "cuisine": "American", "budget": "Moderate", "vegetarian": False},
    ]

    recommended_restaurants = []
    for restaurant in restaurants:
        if restaurant["budget"] == budget and restaurant["vegetarian"] == preferences:
            recommended_restaurants.append(restaurant)

    return recommended_restaurants

budget = input("Enter your budget (Affordable, Moderate, Expensive): ")
preferences = input("Are you looking for vegetarian options? (yes or no): ").lower() == 'yes'


recommended_restaurants = recommend_restaurants(budget, preferences)

if recommended_restaurants:
    print("Recommended Restaurants:")
    for restaurant in recommended_restaurants:
        print(f"{restaurant['name']} - Cuisine: {restaurant['cuisine']}")
else:
    print("Sorry, no restaurants match your criteria.")