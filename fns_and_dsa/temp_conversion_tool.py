# Define Global Conversion Factors
# Factor for converting from Fahrenheit to Celsius: (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Factor for converting from Celsius to Fahrenheit: (9/5)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Formula: C = (F - 32) * (5/9)
    """
    # Accessing the global factor without the 'global' keyword is fine since we are only reading it.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Formula: F = C * (9/5) + 32
    """
    # Accessing the global factor
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and displays the conversion result.
    """
    print("--- Temperature Conversion Tool ---")
    
    # 1. Get Temperature Input
    try:
        temp_input = input("Enter the temperature to convert: ")
        # Attempt to convert input to a float immediately
        temperature = float(temp_input)
    except ValueError:
        # Raise the specified error message if the input is not numeric
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # 2. Get Unit Input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # 3. Perform Conversion and Display Result
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
        
    else:
        # Handle invalid unit input
        print("Invalid unit specified. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")