# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. Try, 2. Except, 3. Finally

print()
try :
    Number = int(input("Enter a Number : "))
    print(1 / Number)

except ZeroDivisionError :
    print("You Can't Divide by Zero IDIOT!")

except ValueError :
    print("Enter Only Numbers Please!")

except Exception :
    print("Something Went Wrong")

finally :
    print("Do Something Cleaneup Here!")