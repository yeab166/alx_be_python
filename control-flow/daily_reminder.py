# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium" | "low":
        # valid priority
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _:
        # unknown priority fallback
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' has an unknown priority that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' has an unknown priority. Consider completing it when you have free time."

print(reminder)
