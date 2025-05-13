# Magic Methods = Dunder Methods (Double Underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

print()
print("========== Magic Methods ==========")
class Student :

    def __init__(self, Name, GPA) :
        self.Name = Name
        self.GPA = GPA

    def __str__(self) :
        return f"Name : {self.Name} GPA : {self.GPA}"

    def __eq__(self, Other) :
        return self.Name == Other.Name

    def __gt__(self, Other) :
        return self.GPA > Other.GPA

    def __lt__(self, Other) :
        return self.GPA < Other.GPA

    def __add__(self, Other) :
        return f"{self.GPA + Other.GPA}"

Student1 = Student ("Kadal", 3.4)
Student2 = Student ("Kadal", 2.2)
Student3 = Student ("Mesir", 3.0)

print("----------------------------")
print(Student1)                                             # def __str__(self) :
print(Student1 == Student2)                                 # def __eq__(self, Other) :
print(Student1 > Student2)                                  # def __gt__(self, Other) :
print(Student1 < Student2)                                  # def __lt__(self, Other) :
print(Student1 + Student2)                                  # def __add__(self, Other) :
print(Student1 == Student3)                                 # def __eq__(self, Other) :
print(Student1 > Student3)                                  # def __gt__(self, Other) :
print(Student1 < Student3)                                  # def __lt__(self, Other) :
print(Student1 + Student3)                                  # def __add__(self, Other) :
print("----------------------------")
print(Student2)                                             # def __str__(self) :
print(Student2 == Student3)                                 # def __eq__(self, Other) :
print(Student2 > Student3)                                  # def __gt__(self, Other) :
print(Student2 < Student3)                                  # def __lt__(self, Other) :
print(Student2 + Student3)                                  # def __add__(self, Other) :
print(Student2 == Student1)                                 # def __eq__(self, Other) :
print(Student2 > Student1)                                  # def __gt__(self, Other) :
print(Student2 < Student1)                                  # def __lt__(self, Other) :
print(Student2 + Student1)                                  # def __add__(self, Other) :
print("----------------------------")
print(Student3)                                             # def __str__(self) :
print(Student3 == Student1)                                 # def __eq__(self, Other) :
print(Student3 > Student1)                                  # def __gt__(self, Other) :
print(Student3 < Student1)                                  # def __lt__(self, Other) :
print(Student3 + Student1)                                  # def __add__(self, Other) :
print(Student3 == Student2)                                 # def __eq__(self, Other) :
print(Student3 > Student2)                                  # def __gt__(self, Other) :
print(Student3 < Student2)                                  # def __lt__(self, Other) :
print(Student3 + Student2)                                  # def __add__(self, Other) :
print("----------------------------")

print()
print("========== Example Magic Methods ==========")
class Book :

    def __init__(self, Title, Author, Num_Pages) :
        self.Title = Title
        self.Author = Author
        self.Num_Pages = Num_Pages

    def __str__(self) :
        return f"'{self.Title}' by {self.Author}"

    def __eq__(self, Other) :
        return self.Title == Other.Title and self.Author == Other.Author

    def __lt__(self, Other) :
        return self.Num_Pages < Other.Num_Pages

    def __gt__(self, Other) :
        return self.Num_Pages > Other.Num_Pages

    def __add__(self, Other) :
        return f"{self.Num_Pages + Other.Num_Pages} Pages"

    def __contains__(self, Keyword) :
        return Keyword in self.Title or Keyword in self.Author

    def __getitem__(self, Key) :
        if Key == "Title" :
            return self.Title
        elif Key == "Author" :
            return self.Author
        elif Key == "Num_Pages" :
            return self.Num_Pages
        else :
            return f"Key {Key} Was Not Found!"

Book1 = Book ("Petualangan Kadal", "I.R. Kadaliman", 330)
Book2 = Book ("Muncak Kunam", "d.r. Kunamon", 361)
Book3 = Book ("Setengah Kodal", "H. Kodalimun", 166)
Book4 = Book ("Petualangan Kadal", "I.R. Kadaliman", 176)

print(Book1)                            # def __str__(self) :
print(Book2)                            # def __str__(self) :
print(Book3)                            # def __str__(self) :

print()
print("-------------------------")
print(Book1 == Book2)                          # def __eq__(self, Other) :
print(Book1 == Book4)                          # def __eq__(self, Other) :
print("-------------------------")
print(Book2 < Book3)                           # def __lt__(self, Other) :
print("-------------------------")
print(Book2 > Book3)                           # def __gt__(self, Other) :
print("-------------------------")
print(Book3 + Book4)                           # def __add__(self, Other) :
print("-------------------------")
print("Kodal" in Book3)                        # def __contains__(self, Keyword) :
print("Kunam" in Book3)                        # def __contains__(self, Keyword) :
print("-------------------------")
print(Book1['Title'])                          # def __getitem__(self, Key) :
print(Book2['Title'])                          # def __getitem__(self, Key) :
print(Book3['Title'])                          # def __getitem__(self, Key) :
print("-------------------------")
print(Book1['Author'])                         # def __getitem__(self, Key) :
print(Book2['Author'])                         # def __getitem__(self, Key) :
print(Book3['Author'])                         # def __getitem__(self, Key) :
print("-------------------------")
print(Book1['Num_Pages'])                      # def __getitem__(self, Key) :
print(Book2['Num_Pages'])                      # def __getitem__(self, Key) :
print(Book3['Num_Pages'])                      # def __getitem__(self, Key) :
print("-------------------------")
print(Book1['Cadas'])                          # def __getitem__(self, Key) :
print(Book2['Kadas'])                          # def __getitem__(self, Key) :
print(Book3['Gudal'])                          # def __getitem__(self, Key) :
print("-------------------------")
