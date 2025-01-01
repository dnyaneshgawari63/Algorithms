class Animal:
  def sound(self):
    pass

class Dog:
  def sound(self):
    return "bhau bhau"

class Cat:
  def sound(self):
    return "meaao"

class Bird:
  def sound(self):
    return "chu chu chu"

def make_sound(animal):
  print(animal.sound)
