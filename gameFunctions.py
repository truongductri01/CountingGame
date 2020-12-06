from players import Player, Computer
import time


def winner(player: Player, comp: Player):
    if player.isWinner():
        print("Winner is", player.name)
    elif comp.isWinner():
        print("Winner is", comp.name)


def playerCounting(player: Player, currentNumber, minStep, maxStep):
    allowInputs = [x for x in range(currentNumber + minStep, currentNumber + maxStep + 1)]
    inputNumber = input(
        "{} counting ({} to {} only): ".format(player.name, allowInputs[0], allowInputs[-1]))
    while not inputNumber.isnumeric():
        inputNumber = input("Please enter an acceptable number for {}: ".format(player.name))

    while int(inputNumber) > currentNumber + maxStep or int(inputNumber) < currentNumber + minStep:
        inputNumber = input("from {} to {} only: ".format(allowInputs[0], allowInputs[-1]))
        while not inputNumber.isnumeric():
            inputNumber = input(
                "Please enter an acceptable number for {} ({} to {} only): ".format(player.name, allowInputs[0],
                                                                                    allowInputs[-1]))
    player.number = (int(inputNumber))


def levelOptions():
    '''
    There are 2 options: easy and hard
    If player choose hard: the computer will calculate each move instead of guessing.
    Otherwise: the computer will play naively by guessing
    :return: "easy" or "hard"
    '''

    introduction = '''There are 2 options: EASY and HARD
    If you choose HARD: the computer will calculate each move instead of guessing.
    If you choose EASY: the computer will play naively by guessing
    '''
    print(introduction)

    option = input("What do you choose [ E(e) or H(h) ]: ")
    while option not in ["E", "e", "H", "h"]:
        option = input(
            "Your choice is not valid. Choose either E or e for Easy level, either H or h for Hard level. Please choose: ")

    if option == "E" or option == "e":
        print("\nYou choose EASY level. Good Luck\n")
        return "easy"
    else:
        print("\nYou choose HARD level. How brave!!!\n")
        return "hard"


def isPlayerGoFirst():
    option = input("Do you want to go first [ Y(y) or N(n) ]: ")
    while option not in ["Y", "y", "N", "n"]:
        option = input(
            "Your choice is not valid. Choose either Y, y or N, n Please choose: ")

    if option == "Y" or option == "y":
        return True
    else:
        return False


def startGame(player: Player, comp: Computer, goalNumber, minStep, maxStep):
    print("We will count to {}, with minimum increment: {}, and maximum increment: {}".format(goalNumber, minStep,
                                                                                              maxStep))
    time.sleep(2)
    currentNumber = 0
    level = levelOptions()
    player.number = comp.number = 0

    if isPlayerGoFirst():
        player.isTurn = True
    else:
        comp.isTurn = True
    # start the game:
    while not player.isWinner() and not comp.isWinner():
        print("-------------------------------------")
        print("Current counting is:", currentNumber)
        if player.isTurn:
            playerCounting(player=player, currentNumber=currentNumber, minStep=minStep, maxStep=maxStep)
        else:
            if level == "easy":
                comp.guessNumber(currentNumber)
            else:
                comp.calculateNumber(currentNumber)
            time.sleep(0.5)
            print("{} counts: {} \n".format(comp.name, comp.number))

        # toggle turn
        comp.changeTurn()
        player.changeTurn()

        currentNumber = max(comp.number, player.number)
    else:
        winner(player, comp)


def restart(player, comp, goalNumber, minStep, maxStep):
    option = input("Do you want to replay [ Y(y) or N(n) ]: ")
    while option not in ["Y", "y", "N", "n"]:
        option = input(
            "Your choice is not valid. Choose either Y, y or N, n Please choose: ")

    if option == "Y" or option == "y":
        startGame(player, comp, goalNumber, minStep, maxStep)
