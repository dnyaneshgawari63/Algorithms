#parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("typical their sound")
#child class
class Dog(Animal):
    def speak(self):
        print("woof")


class Cat(Animal):
    def speak(self):
        print("meo")


animals = [Dog("Ramu"), Cat("Chinu")]

for animal in animals:
    animal.speak()
