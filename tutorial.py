'''
A demo game between two Computer
'''
import gameFunctions as gf
from players import Computer
import time


def demoGame():
    # constants
    currentNumber = 0
    minStep = 1
    maxStep = 3
    goalNumber = 10

    # create players
    comp1 = Computer(goalNumber=goalNumber, minStep=minStep, maxStep=maxStep)
    comp2 = Computer(goalNumber=goalNumber, minStep=minStep, maxStep=maxStep)
    comp1.isTurn = True
    comp1.name = "Computer 1"
    comp2.name = "Computer 2"
    print("\n Demo Game!!! \n We will count to 10 \n Start with 0\n")

    loopCounter = 0  # this counter is even means both players already make their moves

    # start the game:
    while currentNumber < goalNumber:
        if comp1.isTurn:
            comp1.guessNumber(currentNumber)
            print("{} counts: {}".format(comp1.name, comp1.number))
        else:
            comp2.guessNumber(currentNumber)
            print("{} counts: {} \n".format(comp2.name, comp2.number))

        currentNumber = max(comp1.number, comp2.number)
        comp1.changeTurn()
        comp2.changeTurn()
        time.sleep(0.5)
        loopCounter += 1

        if loopCounter % 2 == 0:
            print("-------------------------------------")
            print("Current counting is:", currentNumber)
    else:
        gf.winner(comp1, comp2)


def runDemo():
    print("If this is your first time playing this game, let's go through a demoGame.")

    option = input("Is this your first time [ Y(y) or N(n) ]: ")
    while option not in ["Y", "y", "N", "n"]:
        option = input(
            "Your choice is not valid. Choose either Y, y or N, n Please choose: ")

    if option == "Y" or option == "y":
        time.sleep(0.5)
        demoGame()
    else:
        time.sleep(0.5)


if __name__ == '__main__':
    runDemo()
