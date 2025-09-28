from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # get current datetime
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format it
    print(f"Current date and time: {formatted_date}")
    return formatted_date  # return the formatted string

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)  # calculate future date
    formatted_future = future_date.strftime('%Y-%m-%d')  # format it
    print(f"Future date: {formatted_future}")
    return formatted_future  # return the formatted string

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
