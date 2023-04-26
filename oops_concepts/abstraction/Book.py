# Abstraction is a fundamental concept in object-oriented programming that allows you to focus on essential details while hiding unnecessary complexity from users. Here is an example of a Python program that demonstrates the concept of abstraction using a real-life scenario.
#
# Real-Time Scenario: A library management system
#
# In a library management system, there are various entities such as books, authors, and borrowers. Each entity has different attributes, methods, and behaviors. Let's create a simple library management system that illustrates the concept of abstraction.

class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    def get_genre(self):
        return self.genre


# Define a class for borrowers
class Borrower:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone


# Define a class for library
class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def display_books(self):
        for book in self.books:
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("Pages:", book.get_pages())
            print("Genre:", book.get_genre())
            print()

    def display_borrowers(self):
        for borrower in self.borrowers:
            print("Name:", borrower.get_name())
            print("Address:", borrower.get_address())
            print("Email:", borrower.get_email())
            print("Phone:", borrower.get_phone())
            print()


# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218, "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, "Fiction")
book3 = Book("1984", "George Orwell", 328, "Fiction")

# Create some borrowers
borrower1 = Borrower("John Doe", "123 Main St", "johndoe@example.com", "555-1234")
borrower2 = Borrower("Jane Doe", "456 Elm St", "janedoe@example.com", "555-5678")

# Create a library
library = Library()

# Add the books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add the borrowers to the library
library.add_borrower(borrower1)
library.add_borrower(borrower2)

# Display the books and borrowers
library.display_books()
library.display_borrowers()

# In this program, we have defined three classes: Book, Borrower, and Library. The Book and Borrower classes represent the entities of books and borrowers, respectively, while the Library class is the main class that manages the books and borrowers.
#
# Each class has attributes that represent its properties, and methods that represent its behaviors. However, the details of these methods are hidden from the user, who only needs to know how to interact with the class by calling its methods.
#
# For example, the Book class has the attributes title, author, pages, and genre. It also has getter methods (get_title(), get_author(), get_pages(), and get_genre()) that allow the user to retrieve the values of these attributes without knowing how they are implemented.
#
# Similarly, the Library class has methods for adding books and borrowers to the library (add_book() and add_borrower()), and for displaying the books and borrowers in the library (display_books() and display_borrowers()). These methods hide the implementation details of how the books and borrowers are stored and retrieved in the library.
#
# By using abstraction, we can create a program that is easy to understand, maintain, and extend. The user only needs to know how to interact with the classes and their methods, without worrying about the underlying implementation.
#
# In conclusion, abstraction is an important concept in object-oriented programming that allows us to create programs that are easy to use and maintain. By hiding unnecessary complexity from the user and focusing on essential details, we can create programs that are more efficient, scalable, and robust.
