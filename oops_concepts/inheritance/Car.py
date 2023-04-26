# Sure, here's an example of inheritance using a real-world scenario and a Python program to illustrate it.
#
# Scenario:
# Imagine that you're building a software system for a car dealership. You need to track all the cars that are sold, and you also need to keep track of which cars are in inventory. You decide to use object-oriented programming to model the cars as objects, with different properties and methods depending on whether they're sold or in inventory.
#
# Program:
#
# First, let's define a base class called Car that contains the common properties and methods that all cars have:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# This Car class has an __init__ method that takes in the make, model, and year of the car, and initializes those values as instance variables. It also has four methods: get_make, get_model, get_year, and get_description. These methods will be used by both the SoldCar and InventoryCar classes that we'll define next.
#
# Next, let's define a SoldCar class that inherits from the Car class. This class will represent cars that have been sold:

class SoldCar(Car):
    def __init__(self, make, model, year, sale_price):
        super().__init__(make, model, year)
        self.sale_price = sale_price

    def get_sale_price(self):
        return self.sale_price

    def get_profit(self, purchase_price):
        return self.sale_price - purchase_price

    def get_description(self):
        return f"{super().get_description()} (Sold)"

# This SoldCar class also has an __init__ method that takes in the make, model, year, and sale price of the car, and initializes those values as instance variables. Notice that we call the __init__ method of the Car class using the super() function. This is because we want to reuse the initialization logic of the Car class in the SoldCar class.
#
# In addition to the get_make, get_model, get_year, and get_description methods inherited from the Car class, the SoldCar class also has two new methods: get_sale_price and get_profit. These methods will be used to calculate the profit that the dealership made on the sale of the car.
#
# Finally, notice that the get_description method has been overridden in the SoldCar class. This is because we want the description of a sold car to include the word "(Sold)" at the end.
#
# Now let's define an InventoryCar class that also inherits from the Car class. This class will represent cars that are still in inventory:

class InventoryCar(Car):
    def __init__(self, make, model, year, purchase_price):
        super().__init__(make, model, year)
        self.purchase_price = purchase_price

    def get_purchase_price(self):
        return self.purchase_price

    def get_profit(self, sale_price):
        return sale_price - self.purchase_price

    def get_description(self):
        return f"{super().get_description()} (Inventory)"

# The InventoryCar class is very similar to the SoldCar class, but with a few The InventoryCar class is very similar to the SoldCar class, but with a few

car1 = SoldCar("Toyota", "Camry", 2018, 15000)
car2 = InventoryCar("Honda", "Accord", 2020, 20000)

print(car1.get_description())  # Output: 2018 Toyota Camry (Sold)
print(car2.get_description())  # Output: 2020 Honda Accord (Inventory)

print(car1.get_profit(12000))  # Output: 3000
print(car2.get_profit(25000))  # Output: 5000

# In this example, we create two car objects: car1 is a SoldCar object representing a 2018 Toyota Camry that was sold for $15,000, and car2 is an InventoryCar object representing a 2020 Honda Accord that was purchased for $20,000 and is still in inventory.
#
# We then call the get_description method on each object, which returns a string describing the car, including whether it is sold or in inventory.
#
# Finally, we call the get_profit method on each object, passing in the purchase price or sale price of the car as an argument. This method calculates and returns the profit that the dealership made or will make on the sale of the car.
#
# This example shows how inheritance can be used to model real-world objects with different properties and methods, while still reusing common logic defined in a base class.