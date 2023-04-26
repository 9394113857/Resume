# To write a unit test code for the above code, we will use the built-in Python unittest module. The unittest module provides a framework for writing and running tests, allowing you to check if your code is behaving as expected.
#
# Here is an example of how we can write a unit test code for the above code:
import unittest
from oops_concepts.abstraction.Book import Library,Borrower,Book

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218, "Fiction")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, "Fiction")
        self.book3 = Book("1984", "George Orwell", 328, "Fiction")
        self.borrower1 = Borrower("John Doe", "123 Main St", "johndoe@example.com", "555-1234")
        self.borrower2 = Borrower("Jane Doe", "456 Elm St", "janedoe@example.com", "555-5678")
        self.library = Library()

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library.books), 1)
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library.books), 2)

    def test_add_borrower(self):
        self.library.add_borrower(self.borrower1)
        self.assertEqual(len(self.library.borrowers), 1)
        self.library.add_borrower(self.borrower2)
        self.assertEqual(len(self.library.borrowers), 2)

    def test_display_books(self):
        expected_output = "Title: The Great Gatsby\nAuthor: F. Scott Fitzgerald\nPages: 218\nGenre: Fiction\n\nTitle: To Kill a Mockingbird\nAuthor: Harper Lee\nPages: 281\nGenre: Fiction\n\nTitle: 1984\nAuthor: George Orwell\nPages: 328\nGenre: Fiction\n\n"
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.assertEqual(expected_output, self.library.display_books())

    def test_display_borrowers(self):
        expected_output = "Name: John Doe\nAddress: 123 Main St\nEmail: johndoe@example.com\nPhone: 555-1234\n\nName: Jane Doe\nAddress: 456 Elm St\nEmail: janedoe@example.com\nPhone: 555-5678\n\n"
        self.library.add_borrower(self.borrower1)
        self.library.add_borrower(self.borrower2)
        self.assertEqual(expected_output, self.library.display_borrowers())


if __name__ == '__main__':
    unittest.main()

# In this unit test code, we have created a TestLibraryManagementSystem class that inherits from the unittest.TestCase class. We have also defined a setUp method that initializes the necessary objects for testing.
#
# We have then defined four test methods that test the add_book(), add_borrower(), display_books(), and display_borrowers() methods of the Library class. In each test method, we use the assertEqual() method to check if the expected output matches the actual output.
#
# The unittest.main() method runs the tests and outputs the results to the console.
#
# By writing unit tests, we can ensure that our code is working as expected and catch any errors or bugs early in the development process. This helps to improve the quality of our code and make it more robust and reliable.
