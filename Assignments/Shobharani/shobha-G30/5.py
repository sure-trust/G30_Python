budget = float(input("Enter your budget per person (in rupees): "))
preferences = input("Enter any dietary (e.g., vegetarian, vegan, gluten-free): ")
restaurants = [
    {"name": "Pizza Palace", "cuisine": "Italian", "price_range": "medium", "dietary_options": ["vegetarian"]},
    {"name": "The Noodle House", "cuisine": "Asian", "price_range": "low", "dietary_options": ["vegan"]},
    {"name": "The Grill", "cuisine": "American", "price_range": "high", "dietary_options": ["gluten-free"]},
    {"name": "The Green Bowl", "cuisine": "Health Food", "price_range": "medium", "dietary_options": ["vegetarian", "vegan", "gluten-free"]},
]
recommended_restaurants = []
for restaurant in restaurants:
    if (
        restaurant["price_range"] in ["low", "medium"] if budget <= 500 else restaurant["price_range"] == "high"
        and preferences.lower() in restaurant["dietary_options"]
    ):
        recommended_restaurants.append(restaurant)
if recommended_restaurants:
    print("\nHere are some restaurants that match your criteria:")
    for restaurant in recommended_restaurants:
        print(f"- {restaurant['name']} ({restaurant['cuisine']})")
else:
    print("Sorry, no restaurants found that match your criteria")
