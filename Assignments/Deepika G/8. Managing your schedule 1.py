# Get user input for task details
num_tasks = int(input("Enter the number of tasks: "))

tasks = []
for i in range(num_tasks):
    task_name = input(f"Enter the name of task {i + 1}: ")
    deadline = int(input(f"Enter the deadline for task {i + 1} (in days): "))
    importance = int(input(f"Enter the importance of task {i + 1} (on a scale of 1 to 10): "))
    tasks.append({"name": task_name, "deadline": deadline, "importance": importance})

# Prioritize tasks based on deadline and importance
tasks.sort(key=lambda x: (x['deadline'], x['importance']), reverse=True)

# Display prioritized tasks
print("\nPrioritized Task List:")
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task['name']} - Deadline: {task['deadline']} days, Importance: {task['importance']}")
