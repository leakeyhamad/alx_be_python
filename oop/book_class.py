class Book:
    """
    A class to represent a book with a title, author, and publication year,
    implementing several magic methods for enhanced functionality.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: Initializes a new Book instance.

        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly string for the book.
        This is typically called by built-in functions like print().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that, if passed to eval(), 
        could recreate the object. This is typically called by repr().
        """
        # Note the use of single quotes around string attributes (title, author)
        # to ensure the representation is valid Python code.
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: The provided main.py script will demonstrate the usage of these methods.
# Since the __del__ method is executed upon garbage collection or explicit deletion (del my_book), 
# its execution timing is key to matching the expected output.