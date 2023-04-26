# Sure! Here's an example of how you can write unittest code for the Animal, Dog, and Cat classes we defined in the previous example:
import unittest
from oops_concepts.Method_Overriding.Animal import Animal, Cat, Dog


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Generic Animal", "generic sound")

    def test_animal_name(self):
        self.assertEqual(self.animal.name, "Generic Animal")

    def test_animal_sound(self):
        self.assertEqual(self.animal.sound, "generic sound")

    def test_animal_make_sound(self):
        self.assertEqual(self.animal.make_sound(), "Generic Animal makes generic sound sound.")


class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog("Fido", "woof")

    def test_dog_name(self):
        self.assertEqual(self.dog.name, "Fido")

    def test_dog_sound(self):
        self.assertEqual(self.dog.sound, "woof")

    def test_dog_make_sound(self):
        self.assertEqual(self.dog.make_sound(), "Fido barks.")


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Whiskers", "meow")

    def test_cat_name(self):
        self.assertEqual(self.cat.name, "Whiskers")

    def test_cat_sound(self):
        self.assertEqual(self.cat.sound, "meow")

    def test_cat_make_sound(self):
        self.assertEqual(self.cat.make_sound(), "Whiskers meows.")


if __name__ == '__main__':
    unittest.main()

# In this example, we create three test classes, TestAnimal, TestDog, and TestCat, each of which inherits from unittest.TestCase. We then define a setUp method in each test class, which is called before each test method and creates an instance of the corresponding class (Animal, Dog, or Cat) that we want to test.
#
# We then define a series of test methods for each class, each of which uses assertions to verify that the expected values are equal to the actual values returned by the corresponding method.
#
# Finally, we call the unittest.main() function to run all the test methods in all the test classes.

# When you run this script, you should see output similar to the following:
#
# markdown
# Copy code
# ...
# ----------------------------------------------------------------------
# Ran 9 tests in 0.000s
#
# OK
# The . indicates that each test method passed successfully, and the final output indicates that all 9 tests were run and passed. If any test method fails, the output will indicate which test failed and what the expected and actual values were.
