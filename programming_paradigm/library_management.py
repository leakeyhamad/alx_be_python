# library_management.py

class Book:
    """
    Represents a single book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute for availability (False means available)
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available (not checked out), False otherwise."""
        return not self._is_checked_out

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already available

    def __str__(self):
        """Provides a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        # Private list to store Book instances (Encapsulation)
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
            # print(f"Added: {book.title}")
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """Helper method to find a Book object by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        :param title: The title of the book to check out.
        """
        book = self._find_book(title)
        
        if book:
            if book.check_out():
                print(f"Successfully checked out: {title}")
            else:
                print(f"Error: '{title}' is already checked out.")
        else:
            print(f"Error: Book with title '{title}' not found.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        :param title: The title of the book to return.
        """
        book = self._find_book(title)

        if book:
            if book.return_book():
                print(f"Successfully returned: {title}")
            else:
                print(f"Error: '{title}' was not checked out.")
        else:
            print(f"Error: Book with title '{title}' not found.")

    def list_available_books(self):
        """Prints the title and author of all books that are currently available."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(str(book))
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")