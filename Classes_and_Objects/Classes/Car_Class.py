class Car:
    def __init__(self, make, model, year, color, engine, transmission):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.transmission = transmission
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            print(f"{self.make} {self.model} ({self.year}) is starting")
            self.is_running = True

    def stop(self):
        if self.is_running:
            print(f"{self.make} {self.model} ({self.year}) is stopping")
            self.is_running = False
            self.speed = 0

    def accelerate(self, speed):
        if self.is_running:
            if speed > self.speed:
                print(f"{self.make} {self.model} ({self.year}) is accelerating to {speed} mph")
                self.speed = speed
            elif speed < self.speed:
                print(f"{self.make} {self.model} ({self.year}) is decelerating to {speed} mph")
                self.speed = speed
            else:
                print(f"{self.make} {self.model} ({self.year}) is maintaining speed at {speed} mph")

class Factory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.inventory = []
        self.orders = []

    def order_car(self, make, model, year, color, engine, transmission):
        if len(self.inventory) < self.capacity:
            print(f"Ordering a {color} {year} {make} {model} with a {engine} engine and {transmission} transmission")
            self.orders.append((make, model, year, color, engine, transmission))
        else:
            print(f"Cannot order a car, the factory is at maximum capacity of {self.capacity} cars")

    def produce_car(self):
        if len(self.inventory) > 0:
            print("Producing a car...")
            car = self.inventory.pop(0)
            return car
        elif len(self.orders) > 0:
            print("Producing a car...")
            order = self.orders.pop(0)
            car = Car(*order)
            self.inventory.append(car)
            return car
        else:
            print("Cannot produce a car, the inventory is empty")

    def ship_car(self, car):
        if car in self.inventory:
            print(f"Shipping a {car.color} {car.year} {car.make} {car.model} with a {car.engine} engine and {car.transmission} transmission")
            self.inventory.remove(car)
        else:
            print("Cannot ship a car, it is not in the inventory")

# Creating a car factory with a production capacity of 5 cars
my_factory = Factory(5)

# Ordering 5 cars of different makes, models, years, colors, engines, and transmissions
my_factory.order_car("Toyota", "Corolla", 2022, "silver", "four-cylinder", "automatic")
my_factory.order_car("Honda", "Civic", 2022, "red", "four-cylinder", "manual")
my_factory.order_car("Ford", "Mustang", 2023, "blue", "V8", "manual")
my_factory.order_car("Chevrolet", "Camaro", 2023, "black", "V8", "automatic")
my_factory.order_car("BMW", "M3", 2022, "white", "inline-six", "manual")

# Attempting to order another
my_factory.order_car("Mercedes-Benz", "S-Class", 2023, "gray", "V8", "automatic")

# Producing and shipping 3 cars
car1 = my_factory.produce_car()
my_factory.ship_car(car1)

car2 = my_factory.produce_car()
my_factory.ship_car(car2)

car3 = my_factory.produce_car()
my_factory.ship_car(car3)

# Attempting to produce and ship another car
car4 = my_factory.produce_car()
my_factory.ship_car(car4)

# Creating a Toyota Corolla
my_car = Car("Toyota", "Corolla", 2022, "silver", "four-cylinder", "automatic")

# Starting and accelerating the car
print()
my_car.start()
my_car.accelerate(50)
my_car.accelerate(100)
my_car.accelerate(80)
my_car.stop()

# Creating a Ferrari 458 Italia
my_car = Car("Ferrari", "458 Italia", 2023, "red", "V8", "automatic")

# Starting and accelerating the car
print()
my_car.start()
my_car.accelerate(50)
my_car.accelerate(100)
my_car.accelerate(80)
my_car.stop()

# Creating a BMW X5
my_car = Car("BMW", "X5", 2022, "black", "V8", "automatic")

# Starting and accelerating the car
print()
my_car.start()
my_car.accelerate(30)
my_car.accelerate(60)
my_car.accelerate(45)
my_car.stop()


