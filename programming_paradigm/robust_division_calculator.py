# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division safely, handling ValueError for non-numeric input 
    and ZeroDivisionError.
    
    :param numerator: The numerator, passed as a string from command line.
    :param denominator: The denominator, passed as a string from command line.
    :return: A string containing the result or an error message.
    """
    try:
        # 1. Attempt to convert both inputs to float
        num = float(numerator)
        den = float(denominator)
        
        try:
            # 2. Attempt the division
            result = num / den
            return f"The result of the division is {result}"
        
        except ZeroDivisionError:
            # Catch division by zero
            return "Error: Cannot divide by zero."
            
    except ValueError:
        # Catch errors if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."