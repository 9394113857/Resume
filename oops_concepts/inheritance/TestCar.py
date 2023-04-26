# To write unit tests for the above code, we can use the unittest module in Python. This module provides a set of tools for constructing and running tests. We can create a test class that subclasses unittest.TestCase and define test methods that verify the behavior of our code.
#
# Here's an example of how we could write unit tests for the Car, SoldCar, and InventoryCar classes:
import unittest
from oops_concepts.inheritance.Car import Car,SoldCar,InventoryCar

class TestCar(unittest.TestCase):
    def test_get_description(self):
        car = Car("Toyota", "Camry", 2018)
        self.assertEqual(car.get_description(), "2018 Toyota Camry")

class TestSoldCar(unittest.TestCase):
    def test_get_description(self):
        car = SoldCar("Toyota", "Camry", 2018, 15000)
        self.assertEqual(car.get_description(), "2018 Toyota Camry (Sold)")

    def test_get_profit(self):
        car = SoldCar("Toyota", "Camry", 2018, 15000)
        self.assertEqual(car.get_profit(12000), 3000)

class TestInventoryCar(unittest.TestCase):
    def test_get_description(self):
        car = InventoryCar("Honda", "Accord", 2020, 20000)
        self.assertEqual(car.get_description(), "2020 Honda Accord (Inventory)")

    def test_get_profit(self):
        car = InventoryCar("Honda", "Accord", 2020, 20000)
        self.assertEqual(car.get_profit(25000), 5000)

if __name__ == '__main__':
    unittest.main()

# The error message indicates that there is a problem with the Car class constructor. The constructor is defined with four parameters, but when you create a Car object in the TestCar class, you are passing five arguments: "Toyota", "Camry", 2018, 15000, and an additional argument that is not expected.
#
# To fix this error, you should remove the additional argument from the Car object creation in the TestCar class. Here's the corrected code for the TestCar class:

# In this example, we define three test classes: TestCar, TestSoldCar, and TestInventoryCar. Each test class defines one or more test methods, which use assertions to check that the behavior of the classes is as expected.
#
# For example, the TestCar class defines a single test method test_get_description. This method creates a Car object and calls its get_description method. It then uses the assertEqual method to check that the result of the get_description method is equal to the expected value.
#
# Similarly, the TestSoldCar and TestInventoryCar classes define two test methods each, test_get_description and test_get_profit. These methods create SoldCar and InventoryCar objects and call their respective methods, then use assertions to check that the results are as expected.
#
# We can run these tests by calling the unittest.main() function: