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
# print(dir())
#
# # ------ Example 2 ------
# print()
# print(__name__)
#
# print()
# from Scripts2 import *
#
# print(__name__)
#
# # ------ Example 3 ------
# print()
# def Favourite_Food (Food) :
#     print(f"Your Favourite Food is {Food}")
#
# def Main () :
#     print("This is Scripts1")
#     Favourite_Food("Kadal")
#     print("GoodBye!")
#
# if __name__ == '__main__' :
#     Main ()
#
# # ------ Example 4 ------
# print()
# # Untuk Dirunning pada Scripts 2
# def Favourite_Food (Food) :
#     print(f"Your Favourite Food is {Food}")
#
# print("This is Scripts1")
# Favourite_Food("Kadal")
# print("GoodBye!")
#
# # ------ Example 5 ------
# print()
# def Favourite_Food (Food) :
#     print(f"Your Favourite Food is {Food}")
#
# def Main () :
#     print("This is Scripts1")
#     Favourite_Food("Kadal")
#     print('GoodBye!')
#
# if __name__ == '__main__' :
#     Main ()

# ------ Example 6 ------
print()
def Favourite_Food (Food) :
    print(f"Your Favourite Food is {Food}")

def Main () :
    print("This is Scripts1")
    Favourite_Food("Kadal")
    print('GoodBye!')

if __name__ == '__main__' :
    Main ()