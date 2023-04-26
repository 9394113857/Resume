class DailyUseItem:
    def __init__(self, name, price, brand, is_available):
        self.name = name
        self.price = price
        self.brand = brand
        self.is_available = is_available

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Is Available: {'Yes' if self.is_available else 'No'}")

    def update_availability(self, is_available):
        self.is_available = is_available

# Creating instances of the DailyUseItem class for different items
toothpaste = DailyUseItem("Toothpaste", 2.99, "Colgate", True)
shampoo = DailyUseItem("Shampoo", 5.99, "Pantene", True)
soap = DailyUseItem("Soap", 1.99, "Dove", False)

# Printing information about the items
toothpaste.print_info()
shampoo.print_info()
soap.print_info()

# Updating the availability of an item
soap.update_availability(True)
print(f"Is {soap.name} now available? {'Yes' if soap.is_available else 'No'}")

# In this example, we created instances of the DailyUseItem class for different items,
# and used its methods to print information about them and update their availability.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their attributes and behaviors in a program.

