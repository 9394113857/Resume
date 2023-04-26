class SoftDrink:
    def __init__(self, name, price, brand, flavor, size):
        self.name = name
        self.price = price
        self.brand = brand
        self.flavor = flavor
        self.size = size

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")
        print(f"Flavor: {self.flavor}")
        print(f"Size: {self.size}")

    def update_price(self, price):
        self.price = price

class Cola(SoftDrink):
    def __init__(self, name, price, brand, flavor, size, caffeine_content):
        super().__init__(name, price, brand, flavor, size)
        self.caffeine_content = caffeine_content

    def print_info(self):
        super().print_info()
        print(f"Caffeine Content: {self.caffeine_content}mg")

class Juice(SoftDrink):
    def __init__(self, name, price, brand, flavor, size, fruit_content):
        super().__init__(name, price, brand, flavor, size)
        self.fruit_content = fruit_content

    def print_info(self):
        super().print_info()
        print(f"Fruit Content: {self.fruit_content}%")

# Creating instances of the Cola class for different colas
coca_cola = Cola("Coca-Cola", 25.0, "Coca-Cola Company", "Cola", "250ml", 34)
pepsi = Cola("Pepsi", 20.0, "PepsiCo", "Cola", "200ml", 30)
thums_up = Cola("Thums Up", 30.0, "Coca-Cola Company", "Cola", "300ml", 48)

# Printing information about the colas
coca_cola.print_info()
pepsi.print_info()
thums_up.print_info()

# Updating the price of a cola
coca_cola.update_price(30.0)
print(f"New price of {coca_cola.name} is {coca_cola.price}")

# Creating instances of the Juice class for different juices
orange_juice = Juice("Orange Juice", 40.0, "Tropicana", "Orange", "500ml", 100)
apple_juice = Juice("Apple Juice", 45.0, "Real", "Apple", "1L", 99)
mango_juice = Juice("Mango Juice", 50.0, "Frooti", "Mango", "1.2L", 95)

# Printing information about the juices
orange_juice.print_info()
apple_juice.print_info()
mango_juice.print_info()

# Updating the fruit content of a juice
apple_juice.fruit_content = 90
print(f"New fruit content of {apple_juice.name} is {apple_juice.fruit_content}%")

# I hope this helps you understand how classes and objects can be used to represent different types of soft drinks and their properties.
