# Python File Detection

print()
print("======== Basic File Detection Without Folder ========")
import os

File_Path = "LookupFile.txt"

if os.path.exists(File_Path) :
    print(f"The Location '{File_Path}' Exists")
else :
    print("The Location Doesn't Exist")

print()
print("======== File Detection With Folder ========")
import os

File_Path = "Stuff\DetectionFile.txt"

if os.path.exists(File_Path) :
    print(f"The Location '{File_Path}' Exists")
else :
    print("The Location Doesn't Exist")

print()
print("======== File Detection in My Komputer/Laptop ========")
import os

File_Path = "C:/Users/AzvinaPutri/Desktop/KadalMesirKodal.txt"
File_Path1 = "C:/Users/AzvinaPutri/Desktop/KadalMesirKodal.pdf"

if os.path.exists(File_Path) :
    print(f"The Location '{File_Path}' Exists")
else :
    print("The Location Doesn't Exist")

if os.path.exists(File_Path1) :
    print(f"The Location '{File_Path1}' Exists")
else :
    print("The Location Doesn't Exist")

print()
print("======== Folder Detection in My Komputer/Laptop ========")
import os

File_Path = "C:/Users/AzvinaPutri/Desktop/Love For M3"

if os.path.exists(File_Path) :
    print(f"The Location '{File_Path}' Exists")

    if os.path.isfile(File_Path) :
        print("That is a File")
    elif os.path.isdir(File_Path) :
        print("That is a Directory")

else :
    print("The Location Doesn't Exist")