import time
def introduction():
    txt1 = '''Welcome to COUNTING GAME - A single player game

Rule: Given a goal number, for example: 10
    We will start the game with counting 1 (or 2, or 3).
    Two players (you and the computer) will take turn counting a number,
        who ever reaches or passes number 10 (the goalNumber) first will win.
    '''
    txt2 = '''There are some restrictions when counting:
    1. The first play will count either 1, 2, or 3.
    2. Then for each turn, a player can add 1, 2, or 3
        to the current number to create a new one and count it out.
        For example: player 1 counts 1, then player 2 can either count 2, 3, or 4.
    3. Who counts 10 or a number higher than 10 first will win.
    '''

    time.sleep(1)
    print(txt1)
    time.sleep(3)
    print(txt2)
    time.sleep(3)


if __name__ == '__main__':
    introduction()
