def calculator():
    """
    Prompts the user for two numbers and an operation, then performs the 
    calculation using a Python match-case statement.
    """
    print("Match Case Calculator")
    
    # --- Input Numbers ---
    
        # Prompt user for the first number
    num1= input("Enter the first number: ")
    num1 = float(num1)
        
        # Prompt user for the second number
    num2 = input("Enter the second number: ")
    num2 = float(num2)
  
    
    # --- Input Operation ---
    print("\nChoose the operation:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    operation = input("Choose the operation(+, -, *, /): ").strip()
    
    result = None
    
    # --- Match Case Statement for Calculation ---
    match operation:
        case '+':
            result = num1 + num2
            op_name = "Addition"
        
        case '-':
            result = num1 - num2
            op_name = "Subtraction"
            
        case '*':
            result = num1 * num2
            op_name = "Multiplication"
            
        case '/':
            # Check for division by zero before performing the operation
            if num2 == 0:
                print("\nError: Cannot divide by zero.")
                return # Exit on division by zero error
            result = num1 / num2
            op_name = "Division"
            
        case _:
            # Default case for invalid operation
            print(f"\nError: '{operation}' is an invalid operation choice.")
            return # Exit if operation is invalid
            
    # --- Display Result ---
    # This block executes only if a valid operation was performed successfully
    print(f"\n--- Result ---")
    print(f"Operation: **{op_name}**")
    print(f"Calculation: **{num1} {operation} {num2}**")
    print(f"Result: **{result}**")

# Execute the calculator function when the script is run
if __name__ == "__main__":
    calculator()