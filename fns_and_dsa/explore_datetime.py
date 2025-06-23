from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, no_of_days):
    future_date = current_date + timedelta(days = no_of_days)

    return future_date.strftime("%Y-%m-%d")

no_of_days = int(input("Enter the number of days to add to the current date:"))

print("Future date:",calculate_future_date(display_current_datetime(), no_of_days))
