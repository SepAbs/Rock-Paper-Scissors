from random import *

def Shape(Seq):
    if Seq == "R":
        return "✊"
    elif Seq == "P":
        return "🖐🏻"
    elif Seq == "S":
        return "✌"

def RockPaperScissors(Health1, Health2):
    print("Rock Papaer Scissors guys!")
    #Starting with the starter
    Score1=0
    Score2=0
    Level = 0
    while Level != 3: #Don't use for loops because equality would be ignored as a level.
        CW = choice(["R", "P", "S"])
        Weapon=input("Player1. Choose your weapon. <R, P, S> ")
        while Weapon not in ["R", "P", "S"]:
            Weapon=input("Player1. Choose your weapon. <R, P, S> ")
        print(Shape(CW),"       ",Shape(Weapon))
        if (CW == "R" and Weapon == "P") or (CW == "P" and Weapon == "S") or (CW == "S" and Weapon == "R"):
            print("One point for you!")
            Score1 += 1
            Level += 1
        elif (CW == "P" and Weapon == "R") or (CW == "S" and Weapon == "P") or (CW == "R" and Weapon == "S"):
            print("Oops!")
            Level += 1
        else:
            print("Draw.")
            
    Level = 0
    while Level != 3:
        CW = choice(["R", "P", "S"])
        Weapon=input("Player2. Choose your weapon. <R, P, S> ")
        while Weapon not in ["R", "P", "S"]:
            Weapon=input("Player2. Choose your weapon. <R, P, S> ")
        print(Shape(CW),"       ",Shape(Weapon))
        if (CW == "R" and Weapon == "P") or (CW == "P" and Weapon == "S") or (CW == "S" and Weapon == "R"):
            print("One point for you!")
            Score2 += 1
            Level += 1
        elif (CW == "P" and Weapon == "R") or (CW == "S" and Weapon == "P") or (CW == "R" and Weapon == "S"):
            print("Oops!")
            Level += 1
        else:
            print("Draw.")
        
    if Score1 > Score2:
        print("Starter wins!")
        Health2 -= 10
    elif Score1 < Score2:
        print("Starter lost!")
        Health1 -= 10
    else:
        print("Challenge together again!")
        RockPaperScissors(Health1, Health2)
RockPaperScissors(100, 100)


