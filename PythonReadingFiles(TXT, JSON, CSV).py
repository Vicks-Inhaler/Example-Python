# Python Reading Files (.TXT, .JSON, .CSV)

print()
print("========== .TXT FILE ==========")
print("========== Example Read TXT 1 ==========")
File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

with open(File_Path, "r") as File :
    Content = File.read()
    print(Content)

print()
print("========== .TXT FILE ==========")
print("========== Example Read TXT 2 ==========")
File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.txt"

try :
    with open(File_Path, "r") as File :
        Content = File.read()
        print(Content)

except FileNotFoundError :
    print("That was File Not Found!")

# Note :
# Sekarang setting file Kunamon.txt : File => Properties => Security => Pilih Usernya => Edit => Centang Semua Deny => Klik OK

except PermissionError :
    print("You do not have Permission to Read that File!")

# ===============================================================================

print()
print("========== .JSON FILE ==========")
print("========== Example Read JSON 1 ==========")
import json

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.json"

try :
    with open(File_Path, "r") as File:
        Content = json.load(File)
        print(Content)
        # OR
        print(Content["Name"])
        print(Content["Age"])
        print(Content["Job"])

except FileNotFoundError :
    print("That was File Not Found!")

# Note :
# Sekarang setting file Kunamon.txt : File => Properties => Security => Pilih Usernya => Edit => Centang Semua Deny => Klik OK

except PermissionError :
    print("You do not have Permission to Read that File!")

#=========================================================================================

print()
print("========== .CSV FILE ==========")
print("========== Example Read CSV 1 ==========")
import csv

File_Path = "C:/Users/AzvinaPutri/Desktop/Kunamon.csv"

try :
    with open(File_Path, "r") as File:
        Content = csv.reader(File)
        for Line in Content :
            print(Line)
            # OR
            # print(Line[0])
            # print(Line[1])
            # print(Line[2])

except FileNotFoundError :
    print("That was File Not Found!")

# Note :
# Sekarang setting file Kunamon.txt : File => Properties => Security => Pilih Usernya => Edit => Centang Semua Deny => Klik OK

except PermissionError :
    print("You do not have Permission to Read that File!")