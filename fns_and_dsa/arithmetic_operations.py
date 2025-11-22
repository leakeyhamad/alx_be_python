def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs a basic arithmetic operation (add, subtract, multiply, or divide) 
    on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation, or the string 
                      "Error: Cannot divide by zero" for division by zero.
    """
    
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
            
    else:
        # Handle unrecognized operation string
        return "Error: Invalid operation specified"

