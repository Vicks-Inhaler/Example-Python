# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

print()
print("========== Example 1 ==========")
class Animal :
    def __init__(self, Name) :
        self.Name = Name
        self.Is_Alive = True

    def Eat(self) :
        print(f"{self.Name} is Eating")

    def Sleep(self) :
        print(f"{self.Name} is Sleeping")

class Dog (Animal) :
    pass

class Cat (Animal) :
    pass

class Mouse (Animal) :
    pass

Dog = Dog ("Scooby")
Cat = Cat ("Garfield")
Mouse = Mouse ("Mickey")

print("----------------------")
print(Dog.Name)
print(Dog.Is_Alive)
Dog.Eat()
Dog.Sleep()
print("----------------------")
print(Cat.Name)
print(Cat.Is_Alive)
Cat.Eat()
Cat.Sleep()
print("----------------------")
print(Mouse.Name)
print(Mouse.Is_Alive)
Mouse.Eat()
Mouse.Sleep()
print("----------------------")


print()
print("========== Example 2 ==========")
class Animal :
    def __init__(self, Name) :
        self.Name = Name
        self.Is_Alive = True

    def Eat(self) :
        print(f"{self.Name} is Eating")

    def Sleep(self) :
        print(f"{self.Name} is a Sleep")

class Dog (Animal) :
    def Speak (self) :
        print("WOOF!")

class Cat (Animal) :
    def Speak(self):
        print("MEAW!")

class Mouse (Animal) :
    def Speak(self):
        print("SQUEEK!")

Dog = Dog ("Scooby")
Cat = Cat ("Garfield")
Mouse = Mouse ("Mickey")

Dog.Speak()
Cat.Speak()
Mouse.Speak()