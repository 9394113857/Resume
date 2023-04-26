class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound} sound."


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "bark")

    def make_sound(self):
        return f"{self.name} barks."


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

    def make_sound(self):
        return f"{self.name} meows."
