class Calculator:
    """
    A class demonstrating the use of class methods and static methods.
    """
    # Class Attribute: Accessed by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static Method: Returns the sum of two numbers.
        It does not take 'self' or 'cls' and cannot access class or instance attributes.
        It works like a regular function placed inside the class namespace.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class Method: Returns the product of two numbers.
        It takes 'cls' (the class itself) as the first argument, allowing it 
        to access and modify class-level attributes.
        """
        # Accessing the class attribute 'calculation_type' via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b