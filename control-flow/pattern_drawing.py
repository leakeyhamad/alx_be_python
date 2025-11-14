def print_square_pattern():
    """
    Prompts the user for a size (integer) and prints a square pattern 
    of asterisks (*) of that size.
    """
    
    # --- Input Size ---
   
        # Prompt user and convert input to an integer
    size = int(input("Enter the size of the pattern: "))
    
    # 2. Condition: The loop runs as long as the counter is less than the size
    while row_count < size:
        
        # Action: Print the row of asterisks using string multiplication
        # This effectively prints the column pattern for one row.
        print("*" * size)
        
        # 3. Update: Increment the counter to move to the next row
        row_count += 1
    
    # --- Generate Pattern using Nested Loops ---
    # 1. Outer loop controls the rows
   # for i in range(size):
        # 2. Inner loop controls the columns (the characters in each row)
        #    We want to print 'size' number of '*' characters in a single line.
        
        # A simple way to print the same character 'size' times and add a newline:
        #print("*" * size)
        
        # Alternative method using an inner loop (more explicit):
        # row_output = ""
        # for j in range(size):
        #     row_output += "*"
        # print(row_output)


# Execute the function when the script is run
if __name__ == "__main__":
    print_square_pattern()