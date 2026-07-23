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
    6. Block closed 3
    7. Get closed 3
    8. Get 2 in a row
    9. Place randomly
    '''
    scanned = []
    # Get 5
    scanned.append(sc.generateScan([0,1,1,1,1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,1,1,-1], g.botColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Block closed 4
    scanned.append(sc.generateScan([0,1,1,1,1,-1], g.playerColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Get closed/open 4
    scanned.append(sc.generateScan([0,1,1,1,0,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,1,0,-1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,1,-1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,1,-1,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,1,-1,-1], g.botColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Block open 3
    scanned.append(sc.generateScan([0,1,1,1,0,0], g.playerColor))
    scanned.append(sc.generateScan([0,1,1,1,0,-1], g.playerColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Get Open 3
    scanned.append(sc.generateScan([0,1,1,0,0,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,0,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,0,-1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,1,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,1,-1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,-1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,-1,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,0,-1,-1], g.botColor))
    for item in scanned:
        print(item)
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Block closed 3
    scanned.append(sc.generateScan([0,1,1,1,-1,0], g.playerColor))
    scanned.append(sc.generateScan([0,1,1,1,-1,1], g.playerColor))
    scanned.append(sc.generateScan([0,1,1,1,-1,-1], g.playerColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    # Get closed 3
    scanned.append(sc.generateScan([0,1,1,-1,0,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,0,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,0,-1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,1,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,1,-1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,-1,0], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,-1,1], g.botColor))
    scanned.append(sc.generateScan([0,1,1,-1,-1,-1], g.botColor))
    for item in scanned:
        if item != None:
            return item[1][0], item[1][1]
    scanned.clear()
    # Get 2 in a row
    scanned.append(sc.connect2())
    for item in scanned:
        if item != None:
            return item[0], item[1]
    scanned.clear()
    # Place randomly
    return placeRandomly()

def botPlaceStone():
    pos1, pos2 = analyze()
    b.placeStone(pos1, pos2, g.currentPlayer)