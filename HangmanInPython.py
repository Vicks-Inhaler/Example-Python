# Hangman in Python

print()
from WordsList import Words
import random

# Words = ("apple", "orange", "banana", "coconut", "pineapple")             # Diganti dengan WordsList

# Dictionary of Key : ()
Hangman_Art = {0 : ("   ",
                    "   ",
                    "   "),
               1 : (" O ",
                    "   ",
                    "   "),
               2 : (" O ",
                    " | ",
                    "   "),
               3 : (" O ",
                    "/| ",
                    "   "),
               4 : (" O ",
                    "/|\\",
                    "   "),
               5 : (" O ",
                    "/|\\",
                    "/  "),
               6 : (" O  ",
                    "/|\\",
                    "/ \\")}

# print(Hangman_Art[0])

# print()
# for Line in Hangman_Art[0] :
#     print(Line)

def Display_Man (Wrong_Guesses) :
    print()
    print("***********")
    for Line in Hangman_Art [Wrong_Guesses] :
        print(Line)
    print("***********")

def Display_Hint (Hint) :
    print(" ".join(Hint))

def Display_Answer (Answer) :
    print(" ".join(Answer))

def Main () :
    Answer = random.choice(Words)
    Hint = ["_"] * len(Answer)
    Wrong_Guesses = 0
    Guessed_Letters = set ()
    Is_Running = True

    # print()
    # print(Answer)
    # print(Hint)

    while Is_Running :
        Display_Man(Wrong_Guesses)
        Display_Hint(Hint)

        print()
        Guess = input("Enter a Letter : ").lower()

        if len(Guess) != 1 or not Guess.isalpha() :
            print("Invalid Input")
            continue

        if Guess in Guessed_Letters :
            print(f"{Guess} is Already Guessed")
            continue

        Guessed_Letters.add(Guess)

        if Guess in Answer :
            for i in range(len(Answer)) :
                if Answer[i] == Guess :
                    Hint[i] = Guess
        else :
            Wrong_Guesses += 1

        if "_" not in Hint :
            Display_Man(Wrong_Guesses)
            Display_Answer(Answer)
            print()
            print("YOU WIN!")
            Is_Running = False

        elif Wrong_Guesses >= len(Hangman_Art) - 1 :
            Display_Man(Wrong_Guesses)
            Display_Answer(Answer)
            print()
            print("YOU LOSE!")
            Is_Running = False

if __name__ == "__main__" :
    Main ()