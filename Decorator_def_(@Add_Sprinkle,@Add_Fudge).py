# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream ("Vanilla")

print()
print("========== Basic Decorator Func ==========")
def Add_Sprinkles (Func) :
    def Wrapper () :
        print("*You Add Sprinkles 🍓")
        Func ()
    return Wrapper

def Add_Fudge (Func) :
    def Wrapper () :
        print("You Add Fudge 🍆")
        Func ()
    return Wrapper

@Add_Sprinkles
@Add_Fudge
def Get_Ice_Cream () :
    print("Here is Your Ice Cream 🍨")

Get_Ice_Cream ()

print()
print("========== Example Decorator Func ==========")
def Add_Sprinkles (Func) :
    def Wrapper (*Args, **KwArgs) :
        print("*You Add Sprinkles 🍓")
        Func (*Args, **KwArgs)
    return Wrapper

def Add_Fudge (Func) :
    def Wrapper (*Args, **KwArgs) :
        print("You Add Fudge 🍆")
        Func (*Args, **KwArgs)
    return Wrapper

@Add_Sprinkles
@Add_Fudge
def Get_Ice_Cream () :
    print("Here is Your Ice Cream 🍨")

def Get_Ice_Cream1 (Flavor) :
    print(f"Here is Your {Flavor} Ice Cream 🍨")

Get_Ice_Cream ()
Get_Ice_Cream1 ("Vanilla")
Get_Ice_Cream1 ("Chocolate")