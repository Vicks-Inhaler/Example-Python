# Python Slot Machine
import random

print()

def Spin_Row () :
    Symbols = ['💔', '💣', '💦', '💥', '💨']

    return [random.choice(Symbols) for _ in range(3)]

def Print_Row (Row) :
    print()
    print("***********")
    print(" | ".join(Row))
    print("***********")

def Get_Payout (Row, Bet) :
    if Row[0] == Row[1] == Row[2] :
        if Row[0] == '💔' :
            return Bet * 3
        elif Row[0] == '💣' :
            return Bet * 4
        elif Row[0] == '💦' :
            return Bet * 5
        elif Row[0] == '💥' :
            return Bet * 10
        elif Row[0] == '💨' :
            return Bet * 20
    return 0

def Main () :
    Balance = 100

    print("*************************")
    print(" Welcome to Python Slots ")
    print(" Symbols : 💔 💣 💦 💥 💨  ")
    print("*************************")

    while Balance > 0 :
        print()
        print(f"Current Balance : ${Balance}")

        Bet = input("Place Your Bet Amount : ")

        if not Bet.isdigit() :
            print()
            print("Please Enter a Valid Number!")
            continue

        Bet = int(Bet)

        if Bet > Balance :
            print()
            print("Insufficient Funds")
            continue

        if Bet <= 0 :
            print()
            print("Bet Must be Greater Than 0")
            continue

        Balance -= Bet

        Row = Spin_Row ()
        print()
        print("Spinning...\n")
        Print_Row (Row)

        Payout = Get_Payout(Row, Bet)

        if Payout > 0 :
            print(f"You Won ${Payout}")
        else :
            print("Sorry You Lost This Round!")

        Balance += Payout

        print()
        Play_Again = input("Do You Want to Spin Again? (Y/N) : ")

        if Play_Again != 'Y' :
            break

    print()
    print("*************************************")
    print(f"Game Over! Your Final Balance is ${Balance}")
    print("*************************************")

if __name__ == '__main__' :
    Main ()