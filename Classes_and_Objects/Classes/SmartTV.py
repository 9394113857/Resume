class SmartTV:
    def __init__(self, brand, model, year, size, resolution):
        self.brand = brand
        self.model = model
        self.year = year
        self.size = size
        self.resolution = resolution
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


# Creating an instance of the SmartTV class for a Samsung 4K TV
my_tv = SmartTV("Samsung", "4K TV", 2021, "55 inch", "3840 x 2160")

# Turning on the TV
my_tv.turn_on()

# Opening the Netflix app
my_tv.open_app("Netflix")

# Closing the Netflix app
my_tv.close_app()

# Turning off the TV
my_tv.turn_off()

# In this example, we created an instance of the SmartTV class for a Samsung 4K TV,
# and used its methods to turn it on and off, and open and close apps.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their behaviors in a program.
