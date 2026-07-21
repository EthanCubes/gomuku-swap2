import globalData as g
from random import randint
import board as b
import win as w
import copy

def placeRandomly():
    valid = False
    while not valid:
        pos1 = randint(0, 14)
        pos2 = randint(0, 14)
        if g.boardPositions[pos2][pos1] == 0:
            valid = True
    return pos1, pos2

def analyze():
    '''
    ***Roadmap***
    Scan for immediate danger/win
    Place to create threats/thwart ones
    Place randomly because why not
    '''
    testBoard = copy.deepcopy(g.boardPositions)
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.botColor
                if w.generateScan(testBoard) == g.botColor:
                    return x,y
                testBoard[y][x] = 0
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.playerColor
                if w.generateScan(testBoard) == g.playerColor:
                    return x,y
                testBoard[y][x] = 0
    return placeRandomly()
                


def botPlaceStone():
    pos1, pos2 = analyze()
    print(pos1, pos2)
    b.placeStone(pos1, pos2, g.currentPlayer)