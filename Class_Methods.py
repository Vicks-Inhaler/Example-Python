# Class Methods = Allow operations related to the class itself
#                 Take (cls/self) as the first parameter, which represent the class itself

# Instance Methods = Best for operations on instances of the class (object)
# Static Methods = Best for utility functions that do not need access to class data
# Class Methods = Best for class-level data or require access to the class itself

print()
print("========== Class Methods ==========")
class Student :

    Count = 0
    Total_GPA = 0

    def __init__(self, Name, GPA) :
        self.Name = Name
        self.GPA = GPA
        Student.Count += 1
        Student.Total_GPA += GPA

    # INSTANCE METHOD
    def Get_Info (self) :
        return f"{self.Name} {self.GPA}"

    @classmethod
    def Get_Count (cls) :
        return f"Total # of Student : {cls.Count}"

    @classmethod
    def Get_Average_GPA (cls) :
        if cls.Count == 0 :
            return 0
        else :
            return f"Average GPA : {cls.Total_GPA / cls.Count :.2f}"

Student1 = Student ("Kadal", 3.3)
Student2 = Student ("Mesir", 2.7)
Student3 = Student ("Kodal", 4.0)

print(Student.Get_Count())
print(Student.Get_Average_GPA())