import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Simplified unit tests for the SimpleCalculator class, 
    using a generic test method for each function.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

# --- Generic Test Methods ---

    def test_add(self):
        """Test the addition method with various inputs (positive, negative, zero, float)."""
        # Positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Two negative integers
        self.assertEqual(self.calc.add(-10, -5), -15)
        # Float addition
        self.assertAlmostEqual(self.calc.add(2.5, 1.3), 3.8)
        # Addition with zero
        self.assertEqual(self.calc.add(0, 50), 50)

    def test_subtract(self):
        """Test the subtraction method with various inputs."""
        # Positive result
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Negative result
        self.assertEqual(self.calc.subtract(5, 15), -10)
        # Subtraction involving negatives
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # Float subtraction
        self.assertAlmostEqual(self.calc.subtract(4.2, 1.1), 3.1)
        # Subtraction with zero
        self.assertEqual(self.calc.subtract(50, 0), 50)
    
    def test_multiply(self):
        """Test the multiplication method with various inputs."""
        # Positive result
        self.assertEqual(self.calc.multiply(6, 7), 42)
        # Negative result (one negative factor)
        self.assertEqual(self.calc.multiply(-5, 10), -50)
        # Positive result (two negative factors)
        self.assertEqual(self.calc.multiply(-4, -6), 24)
        # Multiplication by zero
        self.assertEqual(self.calc.multiply(100, 0), 0)
        # Float multiplication
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)

    def test_divide(self):
        """Test the division method, including normal division and division by zero."""
        # Normal division (integer result)
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        # Normal division (float result)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        # Division of zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # CRUCIAL EDGE CASE: Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()