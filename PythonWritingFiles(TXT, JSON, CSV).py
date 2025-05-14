# Python Writing Files (.txt, .json, .csv)

print()
print("========== .TXT FILE ========")
print("========== Writing File in Python Main Program ========")
TXT_Data = "I LIKE KUNAMON"

File_Path = "Kunamon.txt"

with open(File_Path, "w") as File :
    File.write(TXT_Data)
    print(f"TXT File '{File_Path}' was Created")

print()
print("========== .TXT FILE ========")
print("========== Writing File in Desktop PC/Laptop ========")
TXT_Data = "I LIKE KUNAMON!"

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

with open(File_Path, "w") as File :
    File.write(TXT_Data)
    print(f"TXT File '{File_Path}' was Created")

print()
print("========== .TXT FILE ========")
print("========== Writing File With Try, & Except in Desktop PC/Laptop ========")
TXT_Data = "I LIKE KUNAMON!"

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

try :
    with open(File_Path, "a") as File :
        File.write(TXT_Data)
        print(f"TXT File '{File_Path}' was Created")

    #Note :
    # Jika setelah "x" tercreate kemudian dirubah => "a"
    # (Menulis Lagi "I LIKE KUNAMON!" didalam file yang sudah tercreated menjadi "I LIKE KUNAMON! I LIKE KUNAMON! dst")

    # Kemudian  jika "a"/"x" dirubah => "w"
    # (Mengembalikan "I LIKE KUNAMON! I LIKE KUNAMON!" didalam file yang sudah tercreated ke Original File "I LIKE KUNAMON!")

except FileExistsError :
    print("That File Already Exists!")

print()
print("========== .TXT FILE ========")
print("========== Writing File With Try, & Except in Desktop PC/Laptop Per Baris Dibawahnya ========
TXT_Data = "I LIKE KUNAMON!"

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

try :
    with open(File_Path, "a") as File :
        File.write("\n" + TXT_Data)
        print(f"TXT File '{File_Path}' was Created")

except FileExistsError :
    print("That File Already Exists!")

print()
print("========== .TXT FILE ========")
print("========== Example Writing File With Try, & Except in Desktop PC/Laptop ========")
Employees = ["Kadal", "Mesir", "Kodal", "Koplak", "Kunam"]

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

try :
    with open(File_Path, "w") as File :
        for Employee in Employees :
            # File.write(Employee)                              # Dengan Sejajar tanpa spasi
            # File.write(Employee + "\n")                       # Dengan Per Baris Dibawahnya
            File.write(Employee + " ")                          # Dengan Spasi Antar Kata
        print(f"TXT File '{File_Path}' was Created")

except FileExistsError :
    print("That File Already Exists!")

print()
print("========== .JSON FILE ========")
print("========== Example Writing File With Try, & Except in Desktop PC/Laptop ========")
import json

Employees = {"Name" : "Kadal",
             "Age" : 25,
             "Job" : "Programmer"}

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.json"

try :
    with open(File_Path, "w") as File :
        # json.dump(Employees, File)
        json.dump(Employees, File, indent=4)
        print(f"Json File '{File_Path}' was Created")

except FileExistsError :
    print("That File Already Exists!")

print()
print("========== .CSV FILE ========")
print("========== Example Writing File With Try, & Except in Desktop PC/Laptop ========")
import csv

Employees = [["Name", "Age", "Job"],
             ["Kadal", 25, "Programmer"],
             ["Mesir", 20, "UnEmployed"],
             ["Kodal", 28, "Engineer"]]

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.csv"

try :
    # with open(File_Path, "w") as File :                           # Mode Create dengan spasi 1 Space
    with open(File_Path, "w", newline="") as File:                  # Tambahkan newline="" agar Tanpa spasi 1 space
        Writer = csv.writer(File)
        for Row in Employees :
            Writer.writerow(Row)
        print(f"CSV File '{File_Path}' was Created")

except FileExistsError :
    print("That File Already Exists!")