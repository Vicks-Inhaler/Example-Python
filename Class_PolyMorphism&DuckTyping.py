# PolyMorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ARCHIVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods

# "Duck Typing" = Another way to archive polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

print()
print("=========== PolyMorphism ==========")
from abc import ABC, abstractmethod

class Shape :
    @abstractmethod
    def Area (self) :
        pass

class Circle (Shape) :
    def __init__(self, Radius) :
        self.Radius = Radius

    def Area (self) :
        return 3.14 * self.Radius ** 2

class Square (Shape) :
    def __init__(self, Side) :
        self.Side = Side

    def Area (self) :
        return self.Side ** 2

class Triangle (Shape) :
    def __init__(self, Base, Height) :
        self.Base = Base
        self.Height = Height

    def Area (self) :
        return self.Base * self.Height * 0.5

class Pizza (Circle) :
    def __init__(self, Topping, Radius):
        super().__init__(Radius)
        self.Topping = Topping
        # self.Radius = Radius                  # Diganti dengan Super Class karena di Class Circle sudah ada Radius

Shapes = [Circle (4), Square (5), Triangle (6, 7), Pizza ("Peperoni", 15)]

for Shape in Shapes :
    print(f"{Shape.Area()} cm²")

print()
print("=========== Duck Typing ==========")
class Animal :
    Alive = True

class Dog (Animal) :
    def Speak (self) :
        print("WOOF!")

class Cat (Animal) :
    def Speak(self) :
        print("MEOW!")

class Car :

    # Alive = False
    # OR
    Alive = True

    def Speak(self) :
        print("HONK!")

Animals = [Dog (), Cat (), Car ()]

for Animal in Animals :
    Animal.Speak()
    print(Animal.Alive)