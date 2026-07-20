import globals as g
from random import randint
import board as b
from time import sleep

def botScanPosition(basePos, pos1, pos2, pos3, pos4, pattern):
    try:
        basePosStatus = g.boardPositions[basePos[1]][basePos[0]]
        pos1Status = g.boardPositions[pos1[1]][pos1[0]]
        pos2Status = g.boardPositions[pos2[1]][pos2[0]]
        pos3Status = g.boardPositions[pos3[1]][pos3[0]]
        pos4Status = g.boardPositions[pos4[1]][pos4[0]]
        # scan as white
        if basePosStatus == pattern[0]:
            if pos1Status == pattern[1]:
                if pos2Status == pattern[2]:
                    if pos3Status == pattern[3]:
                        if pos4Status == pattern[4]:
                            return 1
        # scan as black
        if basePosStatus == -pattern[0]:
            if pos1Status == -pattern[1]:
                if pos2Status == -pattern[2]:
                    if pos3Status == -pattern[3]:
                        if pos4Status == -pattern[4]:
                            return -1
    except:
        return 0
    return 0

def botGenerateScan(pattern):
    for y in range(15):
        for x in range(15):
            currentPosition = (x, y)
            pos1 = ()
            pos2 = ()
            pos3 = ()
            pos4 = ()
            # N
            pos1 = (x, y + 1)
            pos2 = (x, y + 2)
            pos3 = (x, y + 3)
            pos4 = (x, y + 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            pos4 = (x + 4, y + 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            pos4 = (x + 4, y)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            pos4 = (x + 4, y - 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            pos4 = (x, y - 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            pos4 = (x - 4, y - 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            pos4 = (x - 4, y)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            pos4 = (x - 4, y + 4)
            if botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == 1:
                return 1
            elif botScanPosition(currentPosition, pos1, pos2, pos3, pos4, pattern) == -1:
                return -1
    return 0

def analyze():
    # check for 4 in a row to block, split 2 in a row
    
    # check for ways to get 4 in a row in 1 turn, split 4 in a row
    # check for unblocked 3 in a row to block, split 3 in a row
    # check for ways to get unblocked 3 in a row in 1 turn, split 3 in a row
    # check for ways to make 2x2 square
    return botGenerateScan([1,1,1,1,0])

def botPlaceStone():
    sleep(0.25)
    valid = False
    while not valid:
        pos1 = randint(0, 14)
        pos2 = randint(0, 14)
        if g.boardPositions[pos2][pos1] == 0:
            valid = True
    b.placeStone(pos1, pos2, g.currentPlayer)