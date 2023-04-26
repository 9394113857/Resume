class Bike:
    def __init__(self, make, model, year, color, frame_material, wheel_size):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.frame_material = frame_material
        self.wheel_size = wheel_size
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} ({self.year}) is starting")
        else:
            print(f"{self.make} {self.model} ({self.year}) is already running")

    def accelerate(self, target_speed):
        if self.is_running:
            if target_speed > self.speed:
                print(f"{self.make} {self.model} ({self.year}) is accelerating to {target_speed} mph")
                self.speed = target_speed
            else:
                print(f"{self.make} {self.model} ({self.year}) is decelerating to {target_speed} mph")
                self.speed = target_speed
        else:
            print(f"{self.make} {self.model} ({self.year}) is not running")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.make} {self.model} ({self.year}) is stopping")
        else:
            print(f"{self.make} {self.model} ({self.year}) is not running")


class BikeFactory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.inventory = []

    def order_bike(self, make, model, year, color, frame_material, wheel_size):
        if len(self.inventory) < self.capacity:
            print(f"Ordering a {color} {year} {make} {model} with a {frame_material} frame and {wheel_size}\" wheels")
            self.inventory.append(Bike(make, model, year, color, frame_material, wheel_size))
        else:
            print("Cannot order a bike, the factory is at maximum capacity")

    def produce_bike(self):
        if len(self.inventory) > 0:
            print("Producing a bike...")
            return self.inventory.pop(0)
        else:
            print("Cannot produce a bike, the inventory is empty")

    def ship_bike(self, bike):
        print(
            f"Shipping a {bike.color} {bike.year} {bike.make} {bike.model} with a {bike.frame_material} frame and {bike.wheel_size}\" wheels")

# Creating a bike factory with capacity for 2 bikes
my_factory = BikeFactory(2)

# Ordering three bikes
my_factory.order_bike("Specialized", "Stumpjumper", 2022, "red", "carbon fiber", 29)
my_factory.order_bike("Trek", "Marlin", 2023, "blue", "aluminum", 27.5)
my_factory.order_bike("Giant", "Trance", 2023, "green", "carbon fiber", 29)

# Producing and shipping 2 bikes
bike1 = my_factory.produce_bike()
my_factory.ship_bike(bike1)

bike2 = my_factory.produce_bike()
my_factory.ship_bike(bike2)

# Attempting to produce and ship another bike
bike3 = my_factory.produce_bike()
my_factory.ship_bike(bike3)

# Creating a Cannondale bike instance
my_bike = Bike("Cannondale", "Synapse", 2022, "black", "carbon fiber", 28)

# Starting the bike
my_bike.start()

# Accelerating the bike to 20 mph
my_bike.accelerate(20)

# Accelerating the bike to 30 mph
my_bike.accelerate(30)

# Decelerating the bike to 25 mph
my_bike.accelerate(25)

# Stopping the bike
my_bike.stop()

# Creating a Cannondale bike instance
my_bike = Bike("Cannondale", "Synapse", 2022, "black", "carbon fiber", 28)

# Starting the bike
my_bike.start()

# Accelerating the bike to 20 mph
my_bike.accelerate(20)

# Accelerating the bike to 30 mph
my_bike.accelerate(30)

# Decelerating the bike to 25 mph
my_bike.accelerate(25)

# Stopping the bike
my_bike.stop()
