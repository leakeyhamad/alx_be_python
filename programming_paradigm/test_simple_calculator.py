import unittest
# Assuming simple_calculator.py is in the same directory
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

# --- Test Addition Method ---

    def test_add_two_positive_integers(self):
        """Test addition of two positive integers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_and_positive_integer(self):
        """Test addition involving negative and positive integers."""
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(10, -15), -5)
        self.assertEqual(self.calc.add(-7, 7), 0)

    def test_add_floating_point_numbers(self):
        """Test addition of floating-point numbers."""
        # Using assertAlmostEqual for float comparison to account for precision issues
        self.assertAlmostEqual(self.calc.add(2.5, 1.3), 3.8)
        self.assertAlmostEqual(self.calc.add(-0.1, 0.2), 0.1)

    def test_add_with_zero(self):
        """Test addition when one or both operands are zero."""
        self.assertEqual(self.calc.add(0, 50), 50)
        self.assertEqual(self.calc.add(-42, 0), -42)
        self.assertEqual(self.calc.add(0, 0), 0)

# --- Test Subtraction Method ---

    def test_subtract_two_positive_integers(self):
        """Test subtraction of two positive integers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 15), -10)

    def test_subtract_with_negative_numbers(self):
        """Test subtraction involving negative numbers."""
        # -10 - (-5) = -5
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        # 5 - (-3) = 8
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # -8 - 2 = -10
        self.assertEqual(self.calc.subtract(-8, 2), -10)

    def test_subtract_floating_point_numbers(self):
        """Test subtraction of floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(4.2, 1.1), 3.1)
        self.assertAlmostEqual(self.calc.subtract(10.0, 10.0001), -0.0001)

    def test_subtract_with_zero(self):
        """Test subtraction when one or both operands are zero."""
        self.assertEqual(self.calc.subtract(50, 0), 50)
        self.assertEqual(self.calc.subtract(0, 15), -15)
        self.assertEqual(self.calc.subtract(0, 0), 0)

# --- Test Multiplication Method ---

    def test_multiply_two_positive_integers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_negative_and_positive_integers(self):
        """Test multiplication involving negative and positive integers."""
        self.assertEqual(self.calc.multiply(-5, 10), -50)
        self.assertEqual(self.calc.multiply(3, -9), -27)

    def test_multiply_two_negative_integers(self):
        """Test multiplication of two negative integers."""
        self.assertEqual(self.calc.multiply(-4, -6), 24)

    def test_multiply_with_zero(self):
        """Test multiplication where one or both operands are zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(0, -50), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_floating_point_numbers(self):
        """Test multiplication of floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2), -3.0)

# --- Test Division Method ---

    def test_divide_normal_positive_integers(self):
        """Test division resulting in a whole number and a float."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_divide_by_zero_edge_case(self):
        """Test the crucial division by zero case, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # 0/0 is undefined, should return None as per method spec

    def test_divide_negative_numbers(self):
        """Test division involving negative numbers."""
        # 10 / -2 = -5.0
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        # -10 / 2 = -5.0
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        # -10 / -2 = 5.0
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_zero_numerator(self):
        """Test division when the numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    def test_divide_floating_point_numbers(self):
        """Test division of floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(10.0, 4.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    # This block allows running the tests directly from the script,
    # but the standard command line method is preferred.
    unittest.main()