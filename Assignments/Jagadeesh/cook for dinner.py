#Deciding what to cook for dinner? Write a program that recommends recipes based on available ingredients and dietary restrictions. 
#(Variables: ingredients, restrictions; Operators: ==, !=; If-else: filter recipes based on criteria)

def recommend_recipe(ingredients, restrictions):
    available_recipes = {
        "Pasta with Tomato Sauce": ["pasta", "tomato sauce"],
        "Grilled Chicken Salad": ["chicken", "lettuce", "tomato", "cucumber"],
        "Vegetable Stir-Fry": ["broccoli", "carrot", "bell pepper", "tofu"],
        "Quinoa Bowl": ["quinoa", "black beans", "avocado", "corn"],
    }

    matching_recipes = []

    for recipe, required_ingredients in available_recipes.items():
        if all(ingredient in ingredients for ingredient in required_ingredients) and \
                not any(restriction in recipe for restriction in dietary_restrictions):
            matching_recipes.append(recipe)

    return matching_recipes

# Example usage:
available_ingredients = input("Enter the available ingredients (comma-separated): ").split(", ")
dietary_restrictions = input("Enter dietary restrictions (comma-separated): ").split(", ")

recommended_recipes = recommend_recipe(available_ingredients, dietary_restrictions)

if recommended_recipes:
    print("Recommended Recipes:", recommended_recipes)
else:
    print("No matching recipes found.")
