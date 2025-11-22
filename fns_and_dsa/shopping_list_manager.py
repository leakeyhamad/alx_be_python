def display_menu():
    """Prints the main menu options to the console."""
    # This line now directly prints the required title string:
    print("Shopping List Manager") 
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    
def main():
    """
    The main function that runs the shopping list manager loop.
    It manages the shopping_list and handles user input.
    """
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            ## 1. Add Item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the input isn't just empty space
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
            
        elif choice == '2':
            ## 2. Remove Item
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue

            item = input("Enter the item to remove: ").strip()
            if not item:
                print("Item name cannot be empty.")
                continue

            try:
                # The .remove() method raises a ValueError if the item is not found
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            except ValueError:
                # Catch the error if the item is not in the list
                print(f"'{item}' was not found in the shopping list.")
            
        elif choice == '3':
            ## 3. View List
            if not shopping_list:
                print("Your shopping list is currently empty. Time to start adding items!")
            else:
                print("\nCurrent Shopping List:")
                # Use enumerate to display a numbered list for better readability
                for index, item in enumerate(shopping_list, 1):
                    print(f"  {index}. {item}")
            
        elif choice == '4':
            ## 4. Exit
            print("Thank you for using the Shopping List Manager. Goodbye!")
            break
            
        else:
            ## Invalid Choice Handling
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()