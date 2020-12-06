'''
Create a taking turn system for players
Player 1 goes first.
'''
import random


class Player:
    def __init__(self, isTurn=False, name="Player 1", goalNumber=0):
        self.isTurn = isTurn
        self.number = 0
        self.name = name
        self.goalNumber = goalNumber

    def isWinner(self):
        return self.number >= self.goalNumber

    def changeTurn(self):
        self.isTurn = not self.isTurn


class Computer(Player):
    def __init__(self, goalNumber, minStep, maxStep):
        Player.__init__(self, isTurn=False, name="Computer", goalNumber=goalNumber)
        self.minStep = minStep
        self.maxStep = maxStep
        self.positions = []

    def idealWinningPositions(self):
        startingPoint = self.goalNumber % (self.minStep + self.maxStep)
        positions = [x for x in range(startingPoint, self.goalNumber + 1, self.minStep + self.maxStep)]
        self.positions = positions

    def guessNumber(self, currentNumber):  # Easy level
        self.number = random.randint(currentNumber + self.minStep, currentNumber + self.maxStep)

    def calculateNumber(self, currentNumber):  # Hard level
        self.idealWinningPositions()
        # print(self.positions)
        for i in range(len(self.positions) - 1):
            if self.positions[i] < currentNumber < self.positions[i + 1]:
                if self.minStep <= self.positions[i + 1] - currentNumber <= self.maxStep:
                    print("You have made a big mistake")
                    self.number = self.positions[i + 1]
                else:
                    self.guessNumber(currentNumber)

                break
            elif self.positions[i] > currentNumber:
                if self.minStep <= self.positions[i] - currentNumber <= self.maxStep:
                    print("You will lose my friend")
                    self.number = self.positions[i]
                else:
                    self.guessNumber(currentNumber)

                break
        else:

            print("Guessing")
            self.guessNumber(currentNumber)


if __name__ == '__main__':
    comp = Computer(30, 1, 3)
    comp.calculateNumber(10)
    print(comp.number)
