import globalData as g
from random import randint
import board as b
import win as w
import copy
import massiveChunksOfCopypastaCode as mcocc

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
    # Check for ways to win in 1 turn
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.botColor
                if w.generateScan(testBoard)[1] == g.botColor:
                    return x,y
                testBoard[y][x] = 0
    # Check for 4-in-a-rows to block
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.playerColor
                if w.generateScan(testBoard)[1] == g.playerColor:
                    return x,y
                testBoard[y][x] = 0
    # Check for ways to get 4-in-a-row in one turn
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.botColor
                scan = mcocc.generateScan4(testBoard)
                if scan[0] == g.botColor:
                    if scan[1] == (x,y) or scan[2] == (x,y) or scan[3] == (x,y) or scan[4] == (x,y):
                        return x,y
                testBoard[y][x] = 0
    # Check for any way to block 3-in a rows
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.playerColor
                scan = mcocc.generateScan4(testBoard)
                if scan[0] == g.playerColor:
                    if scan[1] == (x,y) or scan[2] == (x,y) or scan[3] == (x,y) or scan[4] == (x,y):
                        return x,y
                testBoard[y][x] = 0
    # Check for any way to get 3-in-a-row
    for x in range(15):
        for y in range(15):
            if testBoard[y][x] == 0:
                testBoard[y][x] = g.botColor
                scan = mcocc.generateScan3(testBoard)
                if scan[0] == g.botColor:
                    if scan[1] == (x,y) or scan[2] == (x,y) or scan[3] == (x,y):
                        return x,y
                testBoard[y][x] = 0
    if randint(1,100) > 25:
        return mcocc.connect2()
    return placeRandomly()
                


def botPlaceStone():
    pos1, pos2 = analyze()
    b.placeStone(pos1, pos2, g.currentPlayer)