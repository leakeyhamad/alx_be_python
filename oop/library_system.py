## Class Hierarchy demonstrating Inheritance (Book -> EBook, PrintBook)

class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """
        String Representation: Returns a string with the basic book details.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor
        super().__init__(title, author) 
        self.file_size = file_size

    def __str__(self) -> str:
        """
        Overrides the base method to include EBook-specific details.
        """
        # Get base details using super().__str__() and modify/append details
        base_details = super().__str__().replace("Book", "EBook", 1)
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """
        Overrides the base method to include PrintBook-specific details.
        """
        # Get base details using super().__str__() and modify/append details
        base_details = super().__str__().replace("Book", "PrintBook", 1)
        return f"{base_details}, Page Count: {self.page_count}"

## Library class demonstrating Composition

class Library:
    """
    A class that manages a collection of Book objects using Composition, 
    optimized to match the minimal expected output format.
    """
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        """
        Adds a Book instance to the library collection.
        """
        self.books.append(book)
        # REMOVED: print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints only the details of every book, without extra headers/footers.
        """
        # REMOVED: print("\n--- Current Library Collection ---")
        for book in self.books:
            # This calls the correct __str__ method for each book type
            print(book) 
        # REMOVED: print("----------------------------------")