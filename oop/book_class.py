class Book:
    """
    A class to represent a book, implementing required magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: Initializes a new Book instance without printing.
        """
        self.title = title
        self.author = author
        self.year = year
        # REMOVED: print(f"Book '{self.title}' created.") 

    def __del__(self):
        """
        Destructor: Prints the deletion message.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: (title) by (author), published in (year)
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Book('{self.title}', '{self.author}', {self.year})
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"