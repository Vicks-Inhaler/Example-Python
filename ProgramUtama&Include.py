# Example Import
# Module = A File containing code you want to include in your program
#          Use 'import' to include a module (built-in or your own)
#          Usefull to break up a large program reusable separate files

# print(help("module"))

print()
import Include

Result = Include.pi
Result1 = Include.Square(3)
Result2 = Include.Cube(3)
Result3 = Include.Circumference(3)
Result4 = Include.Area(3)

print(Result)
print(Result1)
print(Result2)
print(Result3)
print(Result4)
