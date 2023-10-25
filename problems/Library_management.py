class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []
        # Initialize the number of books to 0
        self.no_books = 0

    def add_book(self, book):
        # Add the book to the list of books
        self.books.append(book)
        # Update the number of books
        self.no_books = len(self.books)

    def show_books(self):
        # Display the total number of books and the book list with serial numbers
        print(f"In this Library, there are a total of {self.no_books} books available")
        print("SrNo.\tBooks")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}\t{book}")

# Create an instance of the Library class
l = Library()

# Add books to the library
l.add_book("Harish")
l.add_book("Sharmistha")
l.add_book("Pallavi")
l.add_book("Joohi")
l.add_book("Harnisha")
l.add_book("Soham")

# Display the list of books in the library
l.show_books()
