# daily_reminder.py

# Step 1: Get user input
task = input("Enter your task: ")
priority = input("Enter priority (High, Medium, Low): ")
time_sensitive = input("Is it time-sensitive? (yes/no): ").lower()

# Step 2: Reaction based on priority using match case
match priority.lower():
    case "high":
        priority_msg = "🚨 High Priority!"
    case "medium":
        priority_msg = "⚡ Medium Priority."
    case "low":
        priority_msg = "✅ Low Priority."
    case _:
        priority_msg = "Priority not recognized."

# Step 3: Modify reminder if time-sensitive
if time_sensitive == "yes":
    time_msg = "This task requires immediate attention!"
else:
    time_msg = "You can handle this task at a convenient time."

# Step 4: Print customized reminder
print(f"Reminder: {task}\n{priority_msg}\n{time_msg}")

