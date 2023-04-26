# To test the above code, we can use the built-in unittest module in Python. Here's an example of how we can write unit tests for the Animal class and its child classes:

import unittest
from oops_concepts.polymorphism.Animal import Animal,Cat,Dog,Bird


class TestAnimal(unittest.TestCase):
    def test_dog_make_sound(self):
        dog = Dog("Tommy")
        self.assertEqual(dog.make_sound(), "Tommy says woof woof!")

    def test_cat_make_sound(self):
        cat = Cat("Kitty")
        self.assertEqual(cat.make_sound(), "Kitty says meow meow!")

    def test_bird_make_sound(self):
        bird = Bird("Polly")
        self.assertEqual(bird.make_sound(), "Polly says tweet tweet!")


if __name__ == '__main__':
    unittest.main()

# In the above code, we define a test class TestAnimal that inherits from unittest.TestCase. We define three test methods test_dog_make_sound(), test_cat_make_sound(), and test_bird_make_sound(), each of which creates an object of the corresponding child class and calls the make_sound() method on it. We use the assertEqual() method to check that the output of the method matches the expected output.
#
# To run the tests, we use the unittest.main() function, which discovers and runs all the test methods in the TestAnimal class.

