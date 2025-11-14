def create_daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity, 
    then generates a customized reminder using match-case and if statements.
    """
    print("Daily Task Reminder Generator")
    print("-" * 35)

    # --- 1. Prompt for Task Details ---
    task = input("Enter your task: ").strip()
    
    # Get priority, convert to lowercase for easier matching
    priority = input("Priority (high/medium/low): ").strip().lower()
    
    # Get time-bound status, convert to lowercase for easier comparison
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Initialize the base message component
    priority_message = ""

    # --- 2. Process Task Based on Priority (Match Case) ---
    match priority:
        case 'high':
            priority_message = "a **high** priority task"
        case 'medium':
            priority_message = "a **medium** priority task"
        case 'low':
            priority_message = "a **low** priority task"
        case _:
            # Default case for invalid priority input
            priority_message = "an **unspecified** priority task"

    # Initialize the time-bound action component
    action_required = ""

    # --- 3. Process Task Based on Time Sensitivity (If Statement) ---
    if time_bound == 'yes':
        # Apply the specific message for time-bound tasks
        action_required = " that requires **immediate attention today!**"
    elif time_bound == 'no':
        # Optional: Define a message for non-time-bound tasks
        action_required = " that should be done soon."
    else:
        # Handle invalid time-bound input
        action_required = " (Time sensitivity unclear)."
        
    # --- 4. Provide a Customized Reminder ---
    final_reminder = (
        f"Reminder: **'{task}'** is {priority_message}{action_required}"
    )
    print(f"Reminder: {task} is {priority_message}{action_required}")
    print("\n" + "=" * 10 + " REMINDER " + "=" * 10)
    print(final_reminder)
    print("=" * 30)

# Execute the function when the script is run
if __name__ == "__main__":
    create_daily_reminder()