# Static Methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility function

# Instance Methods = Best for operations on instance of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

print()
class Employee :

    def __init__(self, Name, Position) :
        self.Name = Name
        self.Position = Position

    def Get_Info (self) :
        return f"{self.Name} = {self.Position}"

    @staticmethod
    def Is_Valid_Position (Position) :
        Valid_Positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return Position in Valid_Positions

Employee1 = Employee ("Kadal", "Manager")
Employee2 = Employee ("Mesir", "Cashier")
Employee3 = Employee ("Kodal", "Cook")

print(Employee.Is_Valid_Position("Cook"))
print(Employee.Is_Valid_Position("Engineer"))

print()
print(Employee1.Get_Info())
print(Employee2.Get_Info())
print(Employee3.Get_Info())