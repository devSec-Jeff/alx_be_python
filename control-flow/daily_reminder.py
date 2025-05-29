task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match time_bound.lower():
    case 'yes':
        if priority == "high":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif priority == "medium":
            print("Your project is of medioum priority")
        elif priority == "low":
            print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Priority cannot be determined")
    case 'no':
        print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Error. Time constarint of your task cannot be determined.")
