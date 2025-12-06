import math

class Shape:
    """
    Base class for all shapes. Defines the common interface 'area()'.
    """
    def area(self):
        """
        Raises an error to enforce method overriding in subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    """
    Derived class for a rectangle, calculating area as length * width.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Overrides the base method to calculate the rectangle's area.
        Formula: length × width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class for a circle, calculating area as π * radius².
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """
        Overrides the base method to calculate the circle's area.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)