# Property = Decorator used to define a method as a property (it can be accessed like an attribute)
#            Benefit : Add additional logic when read, write, or delete attributes
#            Gives you getter, setter, and deleter method

print()
print("========== Basic 1 Property ==========")
class Rectangle :
    def __init__(self, Width, Height) :
        self.Width = Width
        self.Height = Height

Rectangle = Rectangle (3, 4)

print(Rectangle.Width)
print(Rectangle.Height)

print()
print("========== Basic 2 Property ==========")
class Rectangle :
    def __init__(self, Width, Height) :
        self._Width = Width
        self._Height = Height

    @property
    def Width (self) :
        pass

    @property
    def Height (self) :
        pass

Rectangle = Rectangle (3, 4)

print(Rectangle._Width)
print(Rectangle._Height)

print()
print("========== Example Property ==========")
class Rectangle :
    def __init__(self, Width, Height) :
        self._Width = Width
        self._Height = Height

    @property
    def Width (self) :
        return f"{self._Width :.1f} cm"

    @property
    def Height (self) :
        return f"{self._Height :.1f} cm"

    @Width.setter
    def Width (self, New_Width) :
        if New_Width > 0 :
            self._Width = New_Width
        else :
            print("Width Must be Greather Than Zero")

    @Height.setter
    def Height (self, New_Height) :
        if New_Height > 0 :
            self._Height = New_Height
        else :
            print("Height Must be Greather Than Zero")

Rectangle = Rectangle (3, 4)

Rectangle.Width = 5
Rectangle.Height = 6

print("--------------------")
print(Rectangle._Width)
print(Rectangle._Height)
print("--------------------")
print(Rectangle.Width)
print(Rectangle.Height)
print("--------------------")

print()
print("========== Example Deleter Property ==========")
class Rectangle :
    def __init__(self, Width, Height) :
        self._Width = Width
        self._Height = Height

    @property
    def Width (self) :
        return f"{self._Width :.1f} cm"

    @property
    def Height (self) :
        return f"{self._Height :.1f} cm"

    @Width.setter
    def Width (self, New_Width) :
        if New_Width > 0 :
            self._Width = New_Width
        else :
            print("Width Must be Greather Than Zero")

    @Height.setter
    def Height (self, New_Height) :
        if New_Height > 0 :
            self._Height = New_Height
        else :
            print("Height Must be Greather Than Zero")

    @Width.deleter
    def Width (self) :
        del self._Width
        print("Width has been Deleted")

    @Height.deleter
    def Height (self) :
        del self._Height
        print("Height has been Deleter")

Rectangle = Rectangle (3, 4)

Rectangle.Width = 5
Rectangle.Height = 6

del Rectangle.Width
del Rectangle.Height