class Chocolate:
    def __init__(self, name, price, brand, flavor, weight):
        self.name = name
        self.price = price
        self.brand = brand
        self.flavor = flavor
        self.weight = weight

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Flavor: {self.flavor}")
        print(f"Weight: {self.weight}")

    def update_price(self, price):
        self.price = price

class IceCream:
    def __init__(self, name, price, brand, flavor, quantity):
        self.name = name
        self.price = price
        self.brand = brand
        self.flavor = flavor
        self.quantity = quantity

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Flavor: {self.flavor}")
        print(f"Quantity: {self.quantity}")

    def update_quantity(self, quantity):
        self.quantity = quantity

# Creating instances of the Chocolate class for different chocolates
milk_chocolate = Chocolate("Milk Chocolate", 50.0, "Cadbury", "Milk", "100g")
dark_chocolate = Chocolate("Dark Chocolate", 60.0, "Lindt", "Dark", "90g")
white_chocolate = Chocolate("White Chocolate", 40.0, "Nestle", "White", "80g")

# Printing information about the chocolates
milk_chocolate.print_info()
dark_chocolate.print_info()
white_chocolate.print_info()

# Updating the price of a chocolate
milk_chocolate.update_price(60.0)
print(f"New price of {milk_chocolate.name} is {milk_chocolate.price}")

# Creating instances of the IceCream class for different ice creams
vanilla_icecream = IceCream("Vanilla Ice Cream", 30.0, "Amul", "Vanilla", "500ml")
chocolate_icecream = IceCream("Chocolate Ice Cream", 35.0, "Kwality Walls", "Chocolate", "500ml")
strawberry_icecream = IceCream("Strawberry Ice Cream", 40.0, "Mother Dairy", "Strawberry", "500ml")

# Printing information about the ice creams
vanilla_icecream.print_info()
chocolate_icecream.print_info()
strawberry_icecream.print_info()

# Updating the quantity of an ice cream
chocolate_icecream.update_quantity("1L")
print(f"New quantity of {chocolate_icecream.name} is {chocolate_icecream.quantity}")
