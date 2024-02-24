# -*- coding: utf-8 -*-
"""Sai-G30-Python-Assigment-1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wf3bJ-dA97x5DxkSAQV8YBQkBe54ibAh
"""

#1) You're at the grocery store. Write a program to calculate the total bill based on item prices and quantities, applying discounts for bulk purchases. (Variables: prices, quantities; Operators: +, -, *, /; If-else: check bulk quantities for discounts)
prices = {"Lux Soap": 38, "Tooth Paste": 50, "Boast": 150, "Jam": 100}
quantities = {"Lux Soap": 8, "Tooth Paste": 9, "Boast": 2, "Jam": 1}
total_bill = 0
for item, quantity in quantities.items():
   price = prices[item]
   discount =0
   if item == "Lux Soap" and quantity >= 3:
       discount = 0.20
   elif item == "Tooth Paste" and quantity >= 6:
       discount = 0.25
   discounted_price = price * (1 - discount)
   total_bill += discounted_price * quantity
print(f"Total bill: ${total_bill:.2f}")

#2) You have a budget for clothes shopping. Design a program to help you stay within your budget, considering item prices and offering suggestions if you go over. (Variables: budget, item prices; Operators: -, <, >; If-else: check budget vs. total cost)
def budget_clothes_shopping():
   budget = 2000
   total_cost = 0
   num_items = 0
   while True:
       item_price = float(input(" price of an item"))
       if item_price == 0:
           break
       total_cost += item_price
       num_items += 1
       if total_cost > budget:
           print(f"exceeded your budget{total_cost:.2f}")
           break
   if total_cost <= budget:
       print(f"your budget${budget:.2f}.")
budget_clothes_shopping()

#3) Planning a road trip? Write a program to estimate the travel time and fuel cost based on distance, vehicle mileage, and gas prices. (Variables: distance, mileage, gas price; Operators: *, /; If-else: consider different fuel efficiency for highway vs. city driving)
def estimate_travel_time(distance, speed):
  return distance / speed
def estimate_fuel_cost(distance, mileage, gas_price, city_ratio=0.6):
  avg_mileage = (mileage * (1 - city_ratio) + mileage * city_ratio * 0.8)
  gallons_used = distance / avg_mileage
  fuel_cost = gallons_used * gas_price
  return fuel_cost
distance = float(input("Enter travel distance in miles: "))
mileage = float(input("Enter your vehicle's mileage (miles per gallon): "))
gas_price = float(input("Enter current gas price per gallon: "))
highway_ratio = float(input("Enter estimated proportion of highway driving (0-1): "))

highway_speed = float(input("Enter your estimated highway speed (mph): "))
city_speed = float(input("Enter your estimated city speed (mph): "))

highway_time = estimate_travel_time(distance * highway_ratio, highway_speed)
city_time = estimate_travel_time(distance * (1 - highway_ratio), city_speed)
total_time = highway_time + city_time

fuel_cost = estimate_fuel_cost(distance, mileage, gas_price, highway_ratio)

print(f"Estimated travel time (highway): {highway_time:.2f} hours")
print(f"Estimated travel time (city): {city_time:.2f} hours")
print(f"Total estimated travel time: {total_time:.2f} hours")
print(f"Estimated fuel cost: ${fuel_cost:.2f}")

#4) Packing for a camping trip? Create a program that suggests items based on weather conditions and campsite amenities. (Variables: weather, amenities; Operators: ==, !=; If-else: suggest different gear based on conditions)
def camping_trip_packing(weather, amenities):
  suggested_items = []
  if weather == "sun":
    suggested_items.extend(["Hat", "Sunglasses"])
  elif weather == "rain":
    suggested_items.extend(["Raincoat", "Umbrella"])
  if "Dry" in amenities:
    suggested_items.append("Camp fire")
  suggested_items.extend(["Tent", "Sleeping bag", "Cooking", "Water bottle", "Food", "Snacks"])
  return suggested_items
weather = "sun and rain"
amenities = ["Dry"]
suggested_items = camping_trip_packing(weather, amenities)
print(f"Suggested camping gear for {weather} weather with {amenities} amenities:")
for item in suggested_items:
  print(f"- {item}")

# 5)Lost in the city? Design a program that recommends nearby restaurants based on your budget and dietary preferences. (Variables: budget, preferences; Operators: ==, !=; If-else: filter restaurants based on criteria)
budget = int(input("Enter your budget"))
preferences = input("Enter your dietary preferences (e.g. vegetarian, NON-vegetarian")
restaurants = [
    {"name": "Tasty Bites", "cuisine": "Italian", "price_range": "$$", "menu": ["pasta", "pizza", "salad"], "dietary_options": ["vegetarian", "gluten-free"]},
]
def recommend_restaurants(budget, preferences):
    recommended = []
    for restaurant in restaurants:
        if restaurant["price_range"] == "$" and budget >= 10:
            if preferences in restaurant["dietary_options"]:
                recommended.append(restaurant["name"])
        elif restaurant["price_range"] == "$$" and budget >= 20:
            if preferences in restaurant["dietary_options"]:
                recommended.append(restaurant["name"])
        elif restaurant["price_range"] == "$$$" and budget >= 30:
            if preferences in restaurant["dietary_options"]:
                recommended.append(restaurant["name"])
    return recommended
recommended_restaurants = recommend_restaurants(budget, preferences)

if recommended_restaurants:
    print("Recommended restaurants for you:")
    for restaurant in recommended_restaurants:
        print(restaurant)
else:
    print("Sorry, no restaurants match your criteria.")

#6)Choosing an investment plan? Build a program that compares different investment options based on risk tolerance and desired returns. (Variables: risk tolerance, returns; Operators: +, -, *, /; If-else: suggest options based on user's profile)
def investment_plan_suggestions(risk_tolerance, desired_returns):
  suggestions = []
  if risk_tolerance == "low":
    suggestions.append("market funds: Low risk, low returns.")
  elif risk_tolerance == "moderate":
    suggestions.append("Balanced funds:moderate risk and returns.")
  elif risk_tolerance == "high":
    suggestions.append("Growth funds: higher returns and risk.")
  if desired_returns > 10:
    suggestions.append("Consider consulting a financial advisor.")
  return suggestions
risk_tolerance = "moderate"
desired_returns = 2
suggestions = investment_plan_suggestions(risk_tolerance, desired_returns)
print(f"Investment options for {risk_tolerance} risk tolerance and {desired_returns:.2f}% desired returns:")
for suggestion in suggestions:
  print(f"- {suggestion}")

#7)Deciding what to cook for dinner? Write a program that recommends recipes based on available ingredients and dietary restrictions. (Variables: ingredients, restrictions; Operators: ==, !=; If-else: filter recipes based on criteria)
ingredients = ["eggs", "milk", "cheese"]
restrictions = ["vegetarian"]
recipes = [
    {"name": "Omelette", "ingredients": ["eggs", "milk", "cheese"], "dietary_tags": []},
]
recommended_recipes = []
for recipe in recipes:
    if all(ingredient in ingredients for ingredient in recipe["ingredients"]):
        if not restrictions or recipe["dietary_tags"] <= restrictions:
            recommended_recipes.append(recipe)

if recommended_recipes:
    print("Recommended recipes:")
    for recipe in recommended_recipes:
        print(f"- {recipe['name']}")

#8)Planning a workout routine? Design a program that suggests exercises based on fitness level and available equipment. (Variables: fitness level, equipment; Operators: ==, !=; If-else: recommend exercises based on user's needs)
def workout_routine_suggestions(fitness_level, equipment):
  suggestions = []
  if fitness_level == "beginner":
    suggestions.append("Walking")
  elif fitness_level == "intermediate":
    suggestions.append("Jogging")
  if "dumbbells" in equipment:
    suggestions.append("Dumbbell")
  if "weight lift" in equipment:
    suggestions.append("weight lift")
  return suggestions
fitness_level = "beginner"
equipment = ["dumbbells"]
suggestions = workout_routine_suggestions(fitness_level, equipment)
print(f"Workout routine for {fitness_level} level with {equipment}:")
for exercise in suggestions:
  print(f"- {exercise}")

#9)Managing your schedule? Create a program that helps you prioritize tasks based on deadlines and importance. (Variables: deadlines, importance; Operators: <, >; If-else: order tasks based on priority)
class Task:
  def __init__(self, deadline, importance):
    self.deadline = deadline
    self.importance = importance
  def __repr__(self):
    return f"Task(deadline={self.deadline}, importance={self.importance})"
def prioritize_tasks(tasks):
  def sort_key(task):
    return (task.deadline, -task.importance)
  return sorted(tasks, key=sort_key)
tasks = [
  Task(deadline=1, importance=3),
  Task(deadline=3, importance=2),
  Task(deadline=2, importance=5),
  Task(deadline=1, importance=4),
]
print("Original task order:")
for task in tasks:
  print(task)
prioritized_tasks = prioritize_tasks(tasks)
print("\nPrioritized task order:")
for task in prioritized_tasks:
  print(task)

#10)Saving for a goal? Build a program that tracks your progress and suggests adjustments to your saving plan based on your desired timeline. (Variables: goal amount, timeline, current savings; Operators: +, -, *, /; If-else: suggest changes based on progress).
def savings_plan_tracker(goal_amount, timeline, current_savings):
  months_remaining = timeline - (current_savings / goal_amount * timeline)
  monthly_savings_needed = goal_amount / timeline
  progress_info = {
    "goal_amount": goal_amount,
    "timeline": timeline,
    "current_savings": current_savings,
    "months_remaining": months_remaining,
    "monthly_savings_needed": monthly_savings_needed,
  }
  suggestions = {}
  if months_remaining < 0:
    suggestions["message"] = "Congratulations! You've reached your goal early!"
  elif months_remaining > timeline:
    suggestions["message"] = "You're falling behind. Consider increasing your monthly savings."
    suggestions["adjustment"] = monthly_savings_needed - (current_savings / timeline)
  else:
    suggestions["message"] = "You're on track! Keep up the good work."
  return progress_info, suggestions
goal_amount = 10000
timeline = 12
current_savings = 5000
progress_info, suggestions = savings_plan_tracker(goal_amount, timeline, current_savings)
print("Progress information:")
for key, value in progress_info.items():
  print(f"- {key}: {value}")
print("Suggestions:")
for key, value in suggestions.items():
  print(f"- {key}: {value}")

# 11) Medication Reminder: Design a program that reminds patients to take their medication based on dosage and schedule, considering potential interactions if taking multiple medications. (Variables: medication names, dosage, schedule; Operators: +, -, *, /; If-else: check for interactions based on medication types)
num_medications = int(input("Enter the number of medications: "))
for i in range(num_medications):
    medication_name = input(f"Enter the name of Medication {i + 1}: ")
    dosage = float(input(f"Enter the dosage for {medication_name} (in mg): "))
    schedule = input(f"Enter the schedule for {medication_name} (e.g., 'morning', 'afternoon', 'evening'): ")

    print(f"\nReminder for {medication_name}:")

    if schedule.lower() == 'morning':
        print(f"Take {dosage} mg in the morning.")
    elif schedule.lower() == 'afternoon':
        print(f"Take {dosage} mg in the afternoon.")
    elif schedule.lower() == 'evening':
        print(f"Take {dosage} mg in the evening.")
    else:
        print("Invalid schedule provided. Please enter 'morning', 'afternoon', or 'evening'.")

#12)Symptom Checker: Create a program that asks users about their symptoms and suggests possible causes based on a knowledge base, recommending when to seek medical attention. (Variables: symptoms; Operators: ==, !=; If-else: match symptoms to possible causes)
def symptom_checker():
    knowledge_base = {
        "fever": ["common cold", "flu", "infection", "COVID-19"],
        "cough": ["common cold", "flu", "allergies", "pneumonia", "COVID-19"],
        "headache": ["migraine", "tension headache", "dehydration", "sinus infection"],
    }
    user_symptoms = []
    while True:
        symptom = input("Enter a symptom (or type 'done': ")
        if symptom.lower() == "done":
            break
        user_symptoms.append(symptom.lower())
    possible_causes = []
    for symptom in user_symptoms:
        if symptom in knowledge_base:
            possible_causes.extend(knowledge_base[symptom])
    if possible_causes:
        print("Based on your symptoms")
        for cause in set(possible_causes):
            print("Covid", cause)
    else:
        print("I'm not familiar with the symptoms Please consult a doctor.")
symptom_checker()

#13)Grade Calculator: Build a program that calculates student grades based on assignments, exams, and attendance, considering different weighting schemes for different factors. (Variables: grades, weights; Operators: +, -, *, /; If-else: apply different weights based on course policies)
def calculate_grade(assignments, exams, attendance, weights):
  assignment_average = sum(assignments) * weights["assignments"] / len(assignments)
  exam_average = sum(exams) * weights["exams"] / len(exams)
  attendance_contribution = attendance * weights["attendance"]
  final_grade = assignment_average + exam_average + attendance_contribution
  return final_grade
assignments = [80, 95, 78]
exams = [90, 85]
attendance = 92
weights = {"assignments": 0.4, "exams": 0.5, "attendance": 0.1}
final_grade = calculate_grade(assignments, exams, attendance, weights)
print(f"Final grade: {final_grade:.2f}")

#14)College Major Selector: Design a program that helps students choose a college major based on their interests, skills, and job market trends. (Variables: interests, skills, trends; Operators: ==, !=; If-else: match user profile to potential majors)
def college_major_selector():
 interests = input("Enter your interests").split(",")
 skills = input("Enter your skills").split(",")
 trends = {
   "growing": ["Computer Science", "Engineering", "Healthcare",],
   "stable": ["Business", "Education", "Accounting", "Finance"],
 }
 potential_majors = []
 for interest in interests:
   if interest in ["science", "math"]:
     potential_majors.extend(["Computer Science", "Physics", "Mathematics"])
   elif interest in ["business", "finance",]:
     potential_majors.extend(["Business", "Accounting", "Finance",])
 for skill in skills:
   if skill in ["programming", "coding", "problem solving"]:
     potential_majors.append("Computer Science")
   elif skill in ["writing", "communication"]:
     potential_majors.extend(["English","Communications"])
 trending_majors = trends["growing"]
 potential_majors = [major for major in potential_majors if major in trending_majors]
 if potential_majors:
   print("Here are some your match your interests, skills, and trends:")
   for major in potential_majors:
     print(f"- {major}")
 else:
   print("Sorry, I couldn't find your interests or skills, or trends.")
college_major_selector()

#15)Carbon Footprint Calculator: Create a program that estimates an individual's carbon footprint based on their transportation, energy usage, and consumption habits. (Variables: activities, consumption; Operators: +, -, *, /; If-else: calculate footprint based on different factors)
def calculate_carbon_footprint():
  car_emissions = 0.4 * 10 * 365
  public_transport_emissions = 0.2 * 20 * 12
  flight_emissions = 1000
  energy_emissions = 2 * 3000
  red_meat_emissions = 25 * 1 * 52
  food_waste_emissions = 4 * 1 * 52
  clothing_emissions = 5 * 2 * 12
  total_footprint = car_emissions + public_transport_emissions + flight_emissions + energy_emissions + red_meat_emissions + food_waste_emissions + clothing_emissions
  return total_footprint
carbon_footprint = calculate_carbon_footprint()
print("Estimated carbon footprint:", carbon_footprint, "kg CO2 equivalent per year")

#16)Recycling Assistant: Design a program that identifies different types of waste and suggests proper recycling or disposal methods based on local regulations. (Variables: waste type; Operators: ==, !=; If-else: match waste to disposal methods)
def recycling_assistant(waste_type):
  disposal_methods = {
    "paper": "Recycle in blue bin",
    "plastic bottle": "Recycle in blue bin",
    "glass bottle": "Recycle in green bin",
    "food scraps": "Compost or dispose in green bin",
    "yard waste": "Compost or dispose in green bin",
  }
  if waste_type in disposal_methods:
    return disposal_methods[waste_type]
  else:
    return "Please specify the type of waste more accurately."
waste_type = "plastic bottle"
disposal_method = recycling_assistant(waste_type)
print(f"For {waste_type}, you should {disposal_method}.")

#ASSIGNMENT
#PASCALS TRIANGLE
def pascal_triangle(num_rows):
  triangle = []
  for i in range(num_rows):
    row = [1] * (i + 1)
    for j in range(1, i):
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
  return triangle
rows = 6
triangle = pascal_triangle(rows)
for row in triangle:
  print(row)

#1. Write a program that takes an integer as input and determines if it is even or odd using an if-else statement.
def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False
number = int(input("Enter an integer: "))
if is_even(number):
  print(f"{number} is even.")
else:
  print(f"{number} is odd.")

#2. Write a program that takes a person's age as input and determines if they are eligible to vote using an if-else statement.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#3. Write a program that takes a year as input and determines if it is a leap year using an if-else statement.
def is_leap_year(year):
  if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

year = int(input("Enter a year: "))

if is_leap_year(year):
  print(f"{year} is a leap year!")
else:
  print(f"{year} is not a leap year.")

#4. Write a program that takes the price of a product and the discount percentage as input and calculates the discounted price using an if-else statement.
def calculate_discounted_price(price, discount_percentage):
  discount_amount = price * discount_percentage / 100
  discounted_price = price - discount_amount
  return discounted_price
price = float(input("Enter the product price: "))
discount_percentage = float(input("Enter the discount percentage (0-100): "))
discounted_price = calculate_discounted_price(price, discount_percentage)

print(f"The discounted price is: ${discounted_price:.2f}")

#5. Write a program that takes a character as input and determines if it is uppercase or lowercase using an if-else statement.
char = input("Enter a character: ")
if char.isupper():
  print(f"{char} is uppercase.")
else:

  if char.islower():
    print(f"{char} is lowercase.")
  else:
    print(f"{char} is not a letter.")

#6. Write a program that takes a number as input and determines if it is positive, negative
def is_positive(number):
  if number > 0:
    return True
  else:
    return False

numbers = [-5, 0, 10, -2.5, 15.2]
for number in numbers:
  if is_positive(number):
    print(f"{number} is positive.")
  else:
    print(f"{number} is not positive.")

#1.Print a pattern**: Write a Python program to print the following pattern using nested loops:
for i in range(5):
  for j in range(i + 1):
    print("*",end="")
  print()

#2. Write a Python program that prints the multiplication table (from 1 to 10) using nested loops.
for i in range(1, 11):
  for j in range(1, 11):
    product = i * j
    print(f"{product:3d}", end=" ")
  print("")

#3. Write a Python program using nested loops to find all prime numbers within a given range.
def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))
print("Prime numbers between", lower_limit, "and", upper_limit, "are:")
for num in range(lower_limit, upper_limit + 1):
  if is_prime(num):
    print(num)

#4. Write a Python program to print the Fibonacci sequence's first `n` numbers using a loop within a loop.
def print_fibonacci(n):
  if n < 0:
    print("Invalid input: n must be non-negative.")
    return
  a, b = 0, 1
  print(a, b, end=' ')
  for _ in range(2, n):
    c = a + b
    print(c, end=' ')
    a, b = b, c
n = int(input("Enter the number of terms: "))
print_fibonacci(n)

#5. Write a Python program to print Pascal's triangle up to `n` rows using nested loops.
def print_pascal_triangle(n):
  triangle = []
  for row in range(n):
    current_row = [1] * (row + 1)
    for i in range(1, row):
      current_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
    triangle.append(current_row)
  for row in triangle:
    print(" " * (n - len(row)), end="")
    print(*row, sep=" ")
n = int(input("Enter the number of rows: "))
print_pascal_triangle(n)