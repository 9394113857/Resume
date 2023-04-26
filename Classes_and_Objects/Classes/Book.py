class Book:
    def __init__(self, title, author, publisher, year, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author} has been checked in.")
        else:
            print(f"{self.title} is already checked in.")

    def renew(self):
        if self.checked_out:
            print(f"{self.title} by {self.author} has been renewed.")
        else:
            print(f"{self.title} is not checked out.")


# Creating book objects
book1 = Book("The Alchemist", "Paulo Coelho", "HarperCollins", 1988, "9780061122415")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925, "9780743273565")

# Checking out and renewing bookss
book1.check_out()
book1.renew()
book1.check_in()

book2.check_out()
book2.check_out()
book2.check_in()
book2.renew()
