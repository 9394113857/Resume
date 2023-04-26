class KiranaItem:
    def __init__(self, name, price, brand, quantity, category):
        self.name = name
        self.price = price
        self.brand = brand
        self.quantity = quantity
        self.category = category

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Quantity: {self.quantity}")
        print(f"Category: {self.category}")

    def update_quantity(self, quantity):
        self.quantity = quantity


# Creating instances of the KiranaItem class for different items
rice = KiranaItem("Rice", 50.0, "Daawat", "5kg", "Grains")
sugar = KiranaItem("Sugar", 40.0, "Tata", "2kg", "Sweeteners")
salt = KiranaItem("Salt", 20.0, "Tata", "1kg", "Spices")

# Printing information about the items
rice.print_info()
sugar.print_info()
salt.print_info()

# Updating the quantity of an item
salt.update_quantity("500g")
print(f"New quantity of {salt.name} is {salt.quantity}")

# In this example, we created instances of the KiranaItem class for different items,
# and used its methods to print information about them and update their quantity.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their attributes and behaviors in a program.

