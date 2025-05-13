# Class Variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

print()
class Student :
    Class_Years = 2025

    def __init__(self, Name, Age) :
        self.Name = Name
        self.Age = Age

class Pelajar :
    Angkatan = 2020
    No_Pelajar = 0

    def __init__(self, Nama, Umur) :
        self.Nama = Nama
        self.Umur = Umur
        Pelajar.No_Pelajar += 1

Student1 = Student ("Kunam", 20)
Student2 = Student ("Lontong", 19)

Pelajar1 = Pelajar ("Kadal", 25)
Pelajar2 = Pelajar ("Mesir", 22)
Pelajar3 = Pelajar ("Kodal", 22)
Pelajar4 = Pelajar ("Koplak", 28)

print(Student1.Name)
print(Student1.Age)
print(Student1.Class_Years)
print(Student.Class_Years)
print(Student2.Name)
print(Student2.Age)
print(Student2.Class_Years)
print(Student.Class_Years)

print()
print(f"My Graduating  Class of {Pelajar.Angkatan} has {Pelajar.No_Pelajar} Students")
print(Pelajar1.Nama)
print(Pelajar2.Nama)
print(Pelajar3.Nama)
print(Pelajar4.Nama)