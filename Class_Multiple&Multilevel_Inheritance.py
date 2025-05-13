# Multiple Inheritance = Inherit from more than one parent class
#                        C(A, B)

# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                        C(B) <- B(A) <- A

print()
print("========== Multiple Inheritance ==========")
class Animal :
    def Eat (self) :
        print("This Animal is Eating")

    def Sleep (self) :
        print("This Animal is Sleeping")

class Prey (Animal) :
    def Flee(self):
        print("This Animal is Fleeing")

class Predator (Animal) :
    def Hunt (self) :
        print("This Animal is Hunting")

class Rabbit (Prey) :
    pass

class Hawk (Predator) :
    pass

class Fish (Prey, Predator):
    pass

Rabbit = Rabbit ()
Hawk = Hawk ()
Fish = Fish ()

Rabbit.Flee ()
Hawk.Hunt ()
Fish.Flee ()
Fish.Hunt ()

print()
Rabbit.Eat()
Rabbit.Sleep()
Fish.Eat()
Fish.Sleep()

print()
print("========== Multilevel Inheritance ==========")
class Animal :
    def __init__(self, Name) :
        self.Name = Name

    def Eat (self) :
        print(f"{self.Name} is Eating")

    def Sleep (self) :
        print(f"{self.Name} is Sleeping")

class Prey (Animal) :
    def Flee(self):
        print(f"{self.Name} is Fleeing")

class Predator (Animal) :
    def Hunt (self) :
        print(f"{self.Name} is Hunting")

class Rabbit (Prey) :
    pass

class Hawk (Predator) :
    pass

class Fish (Prey, Predator):
    pass

Rabbit = Rabbit ("Kadal")
Hawk = Hawk ("Mesir")
Fish = Fish ("Kodal")

print("------------------------")
Rabbit.Eat ()
Rabbit.Sleep ()
Rabbit.Flee ()
print("------------------------")
Hawk.Eat ()
Hawk.Sleep ()
Hawk.Hunt ()
print("------------------------")
Fish.Eat ()
Fish.Sleep ()
Fish.Flee ()
Fish.Hunt ()
print("------------------------")