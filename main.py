import gameFunctions as gf
from players import Player, Computer
import tutorial
import introduction
import time


def countingGame():
    # TODO: you can change the three constants below and try playing against the computer
    # goalNumber: number where a player need to reach or pass to win
    # minStep: minimum increment when counting
    # maxStep: maximum increment when counting
    # Make sure the condition is met: goalNumber > maxStep > minStep
    minStep = 1
    maxStep = 3
    goalNumber = 10

    if goalNumber > maxStep > minStep:
        playerName = input("What is your name? ")

        # introduction and demo
        introduction.introduction()
        print()
        time.sleep(0.5)
        tutorial.runDemo()
        time.sleep(0.5)
        print()

        # create players
        player = Player(name=playerName, goalNumber=goalNumber)
        comp = Computer(goalNumber=goalNumber, minStep=minStep, maxStep=maxStep)

        # start Game
        gf.startGame(player=player, comp=comp, goalNumber=goalNumber, minStep=minStep, maxStep=maxStep)
        time.sleep(0.5)

        print()
        gf.restart(player=player, comp=comp, goalNumber=goalNumber, minStep=minStep, maxStep=maxStep)

    else:
        print("Make sure the condition is met: goalNumber > maxStep > minStep")


if __name__ == '__main__':
    countingGame()
