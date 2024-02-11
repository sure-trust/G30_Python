#Managing your schedule? Create a program that helps you prioritize tasks based on deadlines and importance.
# (Variables: deadlines, importance; Operators: <, >; If-else: order tasks based on priority)


def prioritize_tasks(tasks):
   
    sorted_tasks = sorted(tasks, key=lambda x: (x['deadline'], x['importance']))
    print("Prioritized Tasks:")
    for task in sorted_tasks:
        print(f"Task: {task['name']}, Deadline: {task['deadline']}, Importance: {task['importance']}")

tasks = [
    {'name': 'Task A', 'deadline': 3, 'importance': 5},
    {'name': 'Task B', 'deadline': 2, 'importance': 7},
    {'name': 'Task C', 'deadline': 1, 'importance': 6},
    {'name': 'Task D', 'deadline': 3, 'importance': 4},
]

prioritize_tasks(tasks)

