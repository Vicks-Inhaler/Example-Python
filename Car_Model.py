class Car :
    def __init__(self, Model, Year, Color, For_Sale) :
        self.Model = Model
        self.Year = Year
        self.Color = Color
        self.For_Sale = For_Sale

# ================================================================
# Mode Methods
class Car_Methods:
    def __init__(self, Model, Year, Color, For_Sale):
        self.Model = Model
        self.Year = Year
        self.Color = Color
        self.For_Sale = For_Sale

    def Drive (self) :
        print("You Drive The Car")
        print(f"You Drive The {self.Model}")
        print(f"You Drive The {self.Color} {self.Model}")

    def Stop (self) :
        print("You Stop The Car")
        print(f"You Stop The {self.Model}")
        print(f"You Stop The {self.Color} {self.Model}")

    def Describe (self) :
        print(f"{self.Year} {self.Color} {self.Model}")