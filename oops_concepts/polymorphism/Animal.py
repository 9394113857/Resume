# Polymorphism is a concept in object-oriented programming that allows objects of different types to be treated as if they are of the same type. In Python, polymorphism can be achieved through method overriding and method overloading.
#
# Let's take a real-time scenario to understand polymorphism. Consider a scenario where we have different types of animals such as dogs, cats, and birds, and each animal can make a sound. We can implement this scenario using polymorphism as follows:
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# class Dog(Animal):
#     def make_sound(self):
#         print(self.name + " says woof woof!")

class Dog(Animal):
    def make_sound(self):
        return self.name + " says woof woof!"


class Cat(Animal):
    def make_sound(self):
        return self.name + " says meow meow!"


class Bird(Animal):
    def make_sound(self):
        return self.name + " says tweet tweet!"


# creating objects of different animals
dog = Dog("Tommy")
cat = Cat("Kitty")
bird = Bird("Polly")

# calling the make_sound method for each animal
dog.make_sound()
cat.make_sound()
bird.make_sound()

# In the above code, we have a parent class Animal with a method make_sound() that is overridden by the child classes Dog, Cat, and Bird. Each child class has its own implementation of the make_sound() method, which allows objects of different types to be treated as if they are of the same type.
#
# When we create objects of different animals and call the make_sound() method, the appropriate implementation of the method is executed based on the type of object. For example, when we call dog.make_sound(), the make_sound() method of the Dog class is executed, which prints "Tommy says woof woof!" to the console.
#
# This is an example of run-time polymorphism, where the appropriate method implementation is determined at runtime based on the type of the object. The Animal class provides a common interface for all the child classes, allowing us to treat objects of different types as if they are of the same type.



############

# Looking at the implementation of the Cat and Bird classes, we can see that both classes are missing a return statement in their make_sound() methods. This means that the methods implicitly return None. To fix the errors, we need to add a return statement to each make_sound() method that returns the string representation of the sound that the animal makes.



