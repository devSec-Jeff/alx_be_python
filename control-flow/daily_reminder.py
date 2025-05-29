task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Your project is of medioum priority")
        else:
            print("Priority cannot be determined")
    case 'low':
        print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Error. Time constarint of your task cannot be determined.")
