class BakeryItem:
    def __init__(self, name, price, type, quantity, description):
        self.name = name
        self.price = price
        self.type = type
        self.quantity = quantity
        self.description = description

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Type: {self.type}")
        print(f"Quantity: {self.quantity}")
        print(f"Description: {self.description}")

    def update_quantity(self, quantity):
        self.quantity = quantity

# Creating instances of the BakeryItem class for different items
bread = BakeryItem("Bread", 25.0, "Loaf", "1pc", "Whole wheat bread")
croissant = BakeryItem("Croissant", 20.0, "Pastry", "1pc", "Buttery flaky pastry")
cupcake = BakeryItem("Cupcake", 10.0, "Cake", "1pc", "Chocolate cupcake with frosting")

# Printing information about the items
bread.print_info()
croissant.print_info()
cupcake.print_info()

# Updating the quantity of an item
croissant.update_quantity("2pcs")
print(f"New quantity of {croissant.name} is {croissant.quantity}")

# In this example, we created instances of the BakeryItem class for different items, and used its methods to print information about them and update their quantity. This demonstrates how classes and objects can be used to represent real-world objects and their attributes and behaviors in a program.

