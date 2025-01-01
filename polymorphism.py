class Animal:
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    return "bhau bhau"

class Cat(Animal):
  def sound(self):
    return "meaao"

class Bird(Animal):
  def sound(self):
    return "chu chu chu"

def make_sound(animal):
  print(animal.sound())

dog = Dog()
cat = Cat()
bird = Bird()

# print result to test above code using below code line
make_sound(cat)
