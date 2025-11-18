from datetime import datetime

def countdown_to_event(event_date):
    now = datetime.now()
    
    # difference between event date and current date
    time_left = event_date - now
    
    # display the remaining days
    
    if time_left.days >= 0:
        print(f"Time left until event: {time_left.days} days")
    elif time_left.days == 0:
        print("The event is Tomorrow!")
    else:
        print(f"The event was {-time_left.days} days ago.")
def main():
    
    print("Event countdown timer")
    event_input = input("Enter the event date (YYYY-MM-DD): ") # e.g., 2023-12-31 which is string format
    try:
        event_date = datetime.strptime(event_input, "%Y-%m-%d") # conveting string to datetime object
        countdown_to_event(event_date) # Calling statement
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

main()