def generate_multiplication_table():
    """
    Prompts the user for a number and prints its multiplication table 
    from 1 up to 10.
    """
    
    # --- Input Number ---
    
        # Prompt user and convert input to an integer
    number_input = input("Enter a number to see its multiplication table: ")
    number = int(number_input)
    
    
    # --- Generate Table using a 'for' loop ---
    # The range(1, 11) generates numbers 1, 2, 3, ..., 10.
    for i in range(1, 11):
        # Calculate the product
        result = number * i
        
        # Print the formatted result using an f-string
        print(f"{number} * {i} = {result}")

# Execute the function when the script is run
if __name__ == "__main__":
    generate_multiplication_table()