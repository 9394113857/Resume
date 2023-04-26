class Laptop:
    def __init__(self, brand, model, year, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.year = year
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.is_on = False
        self.battery_level = 100

    def turn_on(self):
        if not self.is_on:
            print(f"{self.brand} {self.model} ({self.year}) is turning on")
            self.is_on = True
        else:
            print(f"{self.brand} {self.model} ({self.year}) is already on")

    def turn_off(self):
        if self.is_on:
            print(f"{self.brand} {self.model} ({self.year}) is turning off")
            self.is_on = False
        else:
            print(f"{self.brand} {self.model} ({self.year}) is already off")

    def check_battery(self):
        print(f"{self.brand} {self.model} ({self.year}) has {self.battery_level}% battery remaining")

    def charge_battery(self):
        if self.is_on:
            print(f"{self.brand} {self.model} ({self.year}) is on, cannot charge battery")
        else:
            print(f"{self.brand} {self.model} ({self.year}) is charging battery")
            self.battery_level = 100

    def use_app(self, app_name):
        if self.is_on:
            if self.battery_level > 0:
                print(f"{self.brand} {self.model} ({self.year}) is using {app_name}")
                self.battery_level -= 10
            else:
                print(f"{self.brand} {self.model} ({self.year}) is out of battery, cannot use {app_name}")
        else:
            print(f"{self.brand} {self.model} ({self.year}) is off, cannot use {app_name}")


# Creating an instance of the Laptop class for a Dell Inspiron laptop
my_laptop = Laptop("Dell", "Inspiron", 2021, "Intel Core i5", "8 GB", "512 GB SSD")

# Turning on the laptop
my_laptop.turn_on()

# Checking the battery level
my_laptop.check_battery()

# Using the Chrome app
my_laptop.use_app("Chrome")

# Charging the battery
my_laptop.charge_battery()

# Using the Zoom app
my_laptop.use_app("Zoom")

# Turning off the laptop
my_laptop.turn_off()

# In this example, we created an instance of the Laptop class for a Dell Inspiron laptop,
# and used its methods to turn it on and off,
# check and charge its battery level,
# and use different apps.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their behaviors in a program.
