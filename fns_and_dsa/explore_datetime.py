# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Gets the current date and time and prints it in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Use datetime.now() to get the current date and time
    current_date = datetime.now()
    
    # Format the datetime object into the specified string format
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nCurrent date and time: {formatted_current_date}")
    return current_date

def calculate_future_date(current_date: datetime):
    """
    Part 2: Prompts the user for a number of days and calculates the future date.

    Parameters:
        current_date (datetime): The starting datetime object from which to calculate.
    """
    try:
        # Prompt the user for the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for the days.")
        return

    # Create a timedelta object representing the duration
    time_delta = timedelta(days=days_to_add)
    
    # Calculate the future date by adding the timedelta
    future_date = current_date + time_delta
    
    # Format and print only the date part in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    # Part 1: Display current date and time
    # Save the return value to use it as the starting point for Part 2
    current_dt = display_current_datetime()
    
    # Part 2: Calculate the future date
    calculate_future_date(current_dt)