class Calculator:
    """
    A class demonstrating the use of class methods and static methods.
    """
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static Method: Performs addition. No access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b) -> float:
        """
        Class Method: Performs multiplication. Uses 'cls' to access class attributes.
        """
        # Note the use of 'cls' to access the class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b