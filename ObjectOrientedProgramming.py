# Object = A "Bundle" of related attributes (Variables) and methods (Function)
#          Ex. Phone, Cup, Book
#          You need a "Class" to create many objects

# Class = (Blueprint) used to design the structure and layout of an object

print()
class Mobil :
    def __init__(self, Jenis, Tahun, Warna, Dijual) :
        self.Jenis = Jenis
        self.Tahun = Tahun
        self.Warna = Warna
        self.Dijual = Dijual

Mobil1 = Mobil ("Mustang", 2020, "Red", False)
Mobil2 = Mobil ("Avanza", 2022, "Silver", True)
Mobil3 = Mobil ("Expander", 2025, "Black", True)

print(Mobil1.Jenis)
print(Mobil1.Tahun)
print(Mobil1.Warna)
print(Mobil1.Dijual)

print()
print(Mobil2.Jenis)
print(Mobil2.Tahun)
print(Mobil2.Warna)
print(Mobil2.Dijual)

print()
print(Mobil3.Jenis)
print(Mobil3.Tahun)
print(Mobil3.Warna)
print(Mobil3.Dijual)

# ===========================================================================================================
print()
print("---------- Mode Lookup Data Car From Import File ----------")
from Car_Model import Car                                   # Dirubah mengambil data ke File Car_Model.py

Car1 = Car ("Mustang", 2020, "Red", False)
Car2 = Car ("Avanza", 2022, "Silver", True)
Car3 = Car ("Expander", 2025, "Black", True)

print(Car1.Model)
print(Car1.Year)
print(Car1.Color)
print(Car1.For_Sale)

print()
print(Car2.Model)
print(Car2.Year)
print(Car2.Color)
print(Car2.For_Sale)

print()
print(Car3.Model)
print(Car3.Year)
print(Car3.Color)
print(Car3.For_Sale)


# ===========================================================================================================
print()
print("---------- Mode Lookup Data Car From Import File For Mode Methods ----------")
from Car_Model import Car_Methods                                   # Dirubah mengambil data ke File Car_Model.py

Car_Methods1 = Car_Methods ("Mustang", 2020, "Red", False)
Car_Methods2 = Car_Methods ("Avanza", 2022, "Silver", True)
Car_Methods3 = Car_Methods ("Expander", 2025, "Black", True)

Car_Methods1.Drive()
Car_Methods2.Drive()
Car_Methods3.Drive()

print()
Car_Methods1.Stop()
Car_Methods2.Stop()
Car_Methods3.Stop()

print()
Car_Methods1.Describe()
Car_Methods2.Describe()
Car_Methods3.Describe()