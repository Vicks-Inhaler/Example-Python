# Python Banking Program

print()
print("========== Versi 1 ==========")
def Show_Balance () :
    print(f"Your Balance is ${Balance : .2f}")
    print()

def Deposit () :
    Amount = float(input("Enter an Amount to be Deposited : "))
    print()

    if Amount < 0 :
        print("That's Not a Valid Amount")
        print()
        return 0
    else :
        print("Deposited Success!")
        print()
        return Amount

def WithDraw () :
    Amount = float(input("Enter Amount to be WithDraw : "))
    print()

    if Amount > Balance :
        print("Insufficient Funds")
        print()
        return 0
    elif Amount < 0 :
        print("Amount Must be Greater Than 0")
        print()
        return 0
    else :
        print("WithDraw Success!")
        print()
        return Amount

Balance = 0
Is_Running = True

while Is_Running :
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. WithDraw")
    print("4. Exit")

    Choice = input("Enter Your Choice (1-4) : ")
    print()

    if Choice == '1' :
        Show_Balance()
    elif Choice == '2' :
        Balance += Deposit()
    elif Choice == '3' :
        Balance -= WithDraw()
    elif Choice == '4' :
        Is_Running = False
    else :
        print("That is Not a Valid Choice!")

print("Thank You! Have a Nice Day!")

print()
print("========== Versi 2 ==========")
def Show_Balance (Balance) :
    print("*********************************")
    print(f"Your Balance is ${Balance : .2f}")
    print("*********************************")
    print()

def Deposit () :
    print("*********************************")
    Amount = float(input("Enter an Amount to be Deposited : "))
    print("*********************************")
    print()

    if Amount < 0 :
        print("*************************")
        print("That's Not a Valid Amount")
        print("*************************")
        print()
        return 0
    else :
        print("******************")
        print("Deposited Success!")
        print("******************")
        print()
        return Amount

def WithDraw (Balance) :
    print("*************************")
    Amount = float(input("Enter Amount to be WithDraw : "))
    print("*************************")
    print()

    if Amount > Balance :
        print("******************")
        print("Insufficient Funds")
        print("******************")
        print()
        return 0
    elif Amount < 0 :
        print("*****************************")
        print("Amount Must be Greater Than 0")
        print("*****************************")
        print()
        return 0
    else :
        print("*****************")
        print("WithDraw Success!")
        print("*****************")
        print()
        return Amount

def Main () :
    Balance = 0
    Is_Running = True

    while Is_Running :
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. WithDraw")
        print("4. Exit")
        print("*********************")
        print()

        Choice = input("Enter Your Choice (1-4) : ")
        print()

        if Choice == '1' :
            Show_Balance(Balance)
        elif Choice == '2' :
            Balance += Deposit()
        elif Choice == '3' :
            Balance -= WithDraw(Balance)
        elif Choice == '4' :
            Is_Running = False
        else :
            print("***************************")
            print("That is Not a Valid Choice!")
            print("***************************")

    print("***************************")
    print("Thank You! Have a Nice Day!")
    print("***************************")

if __name__ == '__main__' :
    Main ()