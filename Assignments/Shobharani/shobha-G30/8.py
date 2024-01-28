import datetime

tasks = [
    {"task": "Finish project report", "deadline": datetime.date(2024, 1, 30), "importance": 5},
    {"task": "Pay bills", "deadline": datetime.date(2024, 1, 29), "importance": 3},

]

for task in tasks:
    task["urgency"] = task["importance"] / (
        (task["deadline"] - datetime.date.today()).days if task["deadline"] else 1
    )

tasks.sort(key=lambda task: task["urgency"], reverse=True)

print("Prioritized tasks:")
for task in tasks:
    print(f"- {task['task']}")

