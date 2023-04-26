# Method Overriding is a feature of object-oriented programming (OOP) that allows a subclass to provide its own implementation of a method that is already defined in its superclass. In this way, the subclass can modify or extend the behavior of the method inherited from the superclass.
#
# Let's take a real-time scenario to explain Method Overriding. Consider the following code snippet:
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes {self.sound} sound.")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"{self.name} meows.")


# In this example, we have defined a class Animal that has a method make_sound which simply prints the name of the animal and the sound it makes. We then define two subclasses Dog and Cat which inherit from Animal and each of them provides their own implementation of the make_sound method.
#
# When we create an object of Dog or Cat, it will call the respective implementation of make_sound method in the corresponding subclass.
#
# Let's see an example of how this works:
dog = Dog("Fido", "woof")
cat = Cat("Whiskers", "meow")

dog.make_sound() # Output: Fido barks.
cat.make_sound() # Output: Whiskers meows.

# As we can see, the make_sound method of the Animal class is overridden by the make_sound methods of the Dog and Cat subclasses.
#
# In summary, Method Overriding is a powerful feature of OOP that allows subclasses to modify or extend the behavior of a method inherited from a superclass. This enables us to write more flexible and maintainable code that can be customized for specific use cases.

