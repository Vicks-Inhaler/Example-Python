# if __name__ == __main__ : (This script can be imported OR run standalone)
#                           Function and classes in this module can be reused
#                           without the main block of code executing

# Ex. Library = Import library for functionality
#               When running library directly, display, a help page

# # ------ Example 1 ------
# print()
# def Main () :
#     # Your Program Goes Here
#
# if __name__ == '__main__' :
#     Main ()
#
# # ------ Example 2 ------
# print()
# print(__name__)
#
# # ------ Example 3 ------
# print()
# from Scripts1 import *
#
# print(__name__)
#
# # ------ Example 4 ------
# print()
# # Running Scripts 1
# from Scripts1 import *
#
# # ------ Example 5 ------
# print()
# from Scripts1 import *
#
# def Favourite_Drink (Drink) :
#     print(f"Your Favourite Drink is {Drink}")
#
# print("This is Scripts2")
# Favourite_Food("Kunam")
# Favourite_Drink ("Sogem")
# print("GoodBye!")

# ------ Example 6 ------
print()
from Scripts1 import *

def Favourite_Drink (Drink) :
    print(f"Your Favourite Drink is {Drink}")

def Main () :
    print("This is Scripts2")
    Favourite_Food("Kunam")
    Favourite_Drink ("Sogem")
    print("GoodBye!")

if __name__ == '__main__' :
    Main ()