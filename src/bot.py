import globalData as g
from random import randint
import board as b
import win as w
import copy
import scan as sc

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
    *** Roadmap ***
    Scan for immediate danger/win
    Place to create threats/thwart ones
    Place randomly because why not
    *** Order of priority ***
    1. Get 5
    2. Block closed 4
    3. Get close/open 4
    4. Block open 3
    5. Get open 3
    6. Get closed 3
    7. Place randomly
    '''


def botPlaceStone():
    analyze()
    # b.placeStone(pos1, pos2, g.currentPlayer)