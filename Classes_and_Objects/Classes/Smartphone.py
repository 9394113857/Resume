class Smartphone:
    def __init__(self, brand, model, year, color, storage):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.storage = storage
        self.is_on = False
        self.current_app = None

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

    def open_app(self, app_name):
        if self.is_on:
            print(f"{self.brand} {self.model} ({self.year}) is opening {app_name}")
            self.current_app = app_name
        else:
            print(f"{self.brand} {self.model} ({self.year}) is off, cannot open {app_name}")

    def close_app(self):
        if self.is_on and self.current_app is not None:
            print(f"{self.brand} {self.model} ({self.year}) is closing {self.current_app}")
            self.current_app = None
        elif self.is_on:
            print(f"{self.brand} {self.model} ({self.year}) has no app running")
        else:
            print(f"{self.brand} {self.model} ({self.year}) is off, cannot close app")


# Creating an instance of the Smartphone class for an iPhone 12
my_phone = Smartphone("Apple", "iPhone 12", 2021, "black", 128)

# Turning on the phone
my_phone.turn_on()

# Opening the Messages app
my_phone.open_app("Messages")

# Closing the Messages app
my_phone.close_app()

# Turning off the phone
my_phone.turn_off()

# In this example, we created an instance of the Smartphone class for an iPhone 12,
# and used its methods to turn it on and off, and open and close apps.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their behaviors in a program.
