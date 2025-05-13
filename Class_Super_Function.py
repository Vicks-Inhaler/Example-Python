# Super () = Function used in a child class to call methods from a parent class (SuperClass)
#            Allows you to extend the extend the functionality of the inherited methods

print()
print("========== Super Class ==========")
class Shape :
    def __init__(self, Color, Is_Filled):
        self.Color = Color
        self.Is_Filled = Is_Filled

class Circle (Shape) :
    def __init__(self, Color, Is_Filled, Radius) :
        super().__init__(Color, Is_Filled)
        self. Radius = Radius

class Square (Shape) :
    def __init__(self, Color, Is_Filled, Width) :
        super().__init__(Color, Is_Filled)
        self.Width = Width

class Triangle (Shape) :
    def __init__(self, Color, Is_Filled, Width, Height) :
        super().__init__(Color, Is_Filled)
        self.Width = Width
        self.Height = Height

Circle = Circle (Color="Red", Is_Filled=True, Radius=5)
Square = Square (Color="Blue", Is_Filled=False, Width=6)
Triangle = Triangle (Color="Green", Is_Filled=True, Width=7, Height=8)

print("---------------------------")
print(Circle.Color)
print(Circle.Is_Filled)
print(f"{Circle.Radius} cm")
print("---------------------------")
print(Square.Color)
print(Square.Is_Filled)
print(f"{Square.Width} cm")
print("---------------------------")
print(Triangle.Color)
print(Triangle.Is_Filled)
print(f"{Triangle.Width} cm")
print(f"{Triangle.Height} cm")
print("---------------------------")

print()
print("========== Super Class Function ==========")
class Shape :
    def __init__(self, Color, Is_Filled):
        self.Color = Color
        self.Is_Filled = Is_Filled

    def Describe (self) :
        print(f"It is {self.Color} and {'Filled' if self.Is_Filled else 'Not Filled'}")

class Circle (Shape) :
    def __init__(self, Color, Is_Filled, Radius) :
        super().__init__(Color, Is_Filled)
        self. Radius = Radius

    def Describe(self) :
        print(f"It is a Circle with an Area of {3.14 * self.Radius * self.Radius} cm²")
        super().Describe()
        # OR (Jika ingin dibolak-balik)
        # super().Describe()
        # print(f"It is a Circle with an Area of {3.14 * self.Radius * self.Radius} cm²")

class Square (Shape) :
    def __init__(self, Color, Is_Filled, Width) :
        super().__init__(Color, Is_Filled)
        self.Width = Width

    def Describe(self):
        print(f"It is a Square with an Area of {self.Width * self.Width} cm²")
        super().Describe()
        # OR (Jika ingin dibolak-balik)
        # super().Describe()
        # print(f"It is a Square with an Area of {self.Width * self.Width} cm²")

class Triangle (Shape) :
    def __init__(self, Color, Is_Filled, Width, Height) :
        super().__init__(Color, Is_Filled)
        self.Width = Width
        self.Height = Height

    def Describe(self):
        print(f"It is a Triangle with an Area of {self.Height * self.Height / 2} cm²")
        super().Describe()
        # OR (Jika ingin dibolak-balik)
        # super().Describe()
        # print(f"It is a Triangle with an Area of {self.Height * self.Height} cm²")

Circle = Circle (Color="Red", Is_Filled=True, Radius=5)
Square = Square (Color="Blue", Is_Filled=False, Width=6)
Triangle = Triangle (Color="Green", Is_Filled=True, Width=7, Height=8)

Circle.Describe()
Square.Describe()
Triangle.Describe()