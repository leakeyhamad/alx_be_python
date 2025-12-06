## Class Hierarchy demonstrating Inheritance (Book -> EBook, PrintBook)

class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """
        Returns a string with the basic book details.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor
        super().__init__(title, author) 
        self.file_size = file_size # Unique attribute

    def get_details(self) -> str:
        """
        Overrides the base method to include EBook-specific details.
        """
        # Get base details and append EBook details
        base_details = super().get_details().replace("Book", "EBook", 1)
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a physical print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count # Unique attribute

    def get_details(self) -> str:
        """
        Overrides the base method to include PrintBook-specific details.
        """
        # Get base details and append PrintBook details
        base_details = super().get_details().replace("Book", "PrintBook", 1)
        return f"{base_details}, Page Count: {self.page_count}"

## Library class demonstrating Composition

class Library:
    """
    A class that manages a collection of Book objects using Composition.
    """
    def __init__(self):
        # The 'books' list is the component, demonstrating composition
        self.books = [] 

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library collection.
        Due to polymorphism, any object derived from Book can be stored.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of every book in the library.
        Polymorphism ensures the correct get_details method is called for each type.
        """
        print("\n--- Current Library Collection ---")
        for book in self.books:
            print(book.get_details())
        print("----------------------------------")

# Note: The main execution block is in main.py