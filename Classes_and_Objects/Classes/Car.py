class Car:
    # Defining the class attributes
    make = ""
    model = ""
    year = 0

    # Defining the class method
    def start(self):
        print("The car has started.")


# Creating an object of the Car class
my_car = Car()

# Accessing the attributes of the my_car object
my_car.make = "Toyota"
my_car.model = "Camry"
my_car.year = 2020

# Accessing the methods of the my_car object
my_car.start()

# Printing the attributes of the my_car object
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)
