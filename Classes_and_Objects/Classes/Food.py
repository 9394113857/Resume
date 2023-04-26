class Food:
    def __init__(self, name, price, calories, is_vegetarian):
        self.name = name
        self.price = price
        self.calories = calories
        self.is_vegetarian = is_vegetarian

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Calories: {self.calories}")
        print(f"Is Vegetarian: {'Yes' if self.is_vegetarian else 'No'}")

    def calculate_cost_per_calorie(self):
        return self.price / self.calories

# Creating instances of the Food class for different food items
pizza = Food("Pizza", 10.99, 1200, False)
burger = Food("Burger", 8.99, 800, False)
salad = Food("Salad", 6.99, 200, True)

# Printing information about the food items
pizza.print_info()
burger.print_info()
salad.print_info()

# Calculating the cost per calorie for the food items
print(f"Cost per calorie for {pizza.name}: ${pizza.calculate_cost_per_calorie():.2f}")
print(f"Cost per calorie for {burger.name}: ${burger.calculate_cost_per_calorie():.2f}")
print(f"Cost per calorie for {salad.name}: ${salad.calculate_cost_per_calorie():.2f}")

# In this example, we created instances of the Food class for different food items,
# and used its methods to print information about them and calculate their cost per calorie.

# This demonstrates how classes and objects can be used to represent real-world objects
# and their attributes and behaviors in a program.
