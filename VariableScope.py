# Variable Scope = Where a variable is Visible and Accessible
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

print()
print("====== Local Function ======")
def Func1 () :
    A = 1
    print(A)

def Func2 () :
    B = 2
    print(B)

Func1()
Func2()

print()
print("====== Enclosed Function ======")
def Func1 () :
    X = 1
    print(X)

    def Func2():
        X = 2
        print(X)
    Func2()

Func1()

print()
def Func1 () :
    X = 1

    def Func2():
        X = 2
        print(X)
    Func2()

Func1()

print()
def Func1 () :
    X = 1

    def Func2():
        print(X)
    Func2()

Func1()

print()
print("====== Global Function ======")
def Func1 () :
    print(X)

def Func2 () :
    print(X)

X = 3

Func1()
Func2()

print()
def Func1 () :
    X = 1
    print(X)

def Func2 () :
    X = 2
    print(X)

X = 3                               # Tidak ditampilkan karena X sudah dalam bentuk Local Fuction diatasnya

Func1()
Func2()

print()
print("====== Built-in Function ======")
from math import e


def Func1():
    print(e)

print(e)
Func1()

print()
def Func1():
    print(e)

e = 3

print(e)