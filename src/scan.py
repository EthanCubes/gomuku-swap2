import random
import globalData as g

def scanBoard(x, y, pattern): # now this is the hard part.
    reverse = []
    for item in pattern:
        reverse.append(-item)
    dlist = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] # set up scanning in all 8 directions
    scanList = []
    # Gets the status and puts it in a list
    for direction in dlist:
        dirScanList = [] # directional scan
        for i in range(6):
            dirScanList.append((x+i*int(direction[0]), y+i*int(direction[1])))
        statusList = []
        for item in dirScanList:
            if not (item[0] < 0 or item[0] > 14 or item[1] < 0 or item[1] > 14):
                statusList.append(g.boardPositions[item[1]][item[0]])
        scanList.append(statusList)
    # Compares the list to the given pattern
    for item in scanList:
        if item == pattern:
            return 1
        elif item == reverse:
            return -1
    return None

def generateScan(pattern, color): # pattern has to be 6 characters.
    posList = []
    for y in range(15):
        for x in range(15):
            scan = scanBoard(x,y,pattern)
            if scan == -1 or scan == 1:
                posList.append((scan, (x, y))) # Appends to the list color of the combonation and the coordinates.
    whitelist = []
    blacklist = []
    if color != 0:
        for item in posList:
            if item[0] == 1:
                whitelist.append(item)
            else:
                blacklist.append(item)
    else:
        return posList
    if color == 1:
        return whitelist
    elif color == -1:
        return blacklist

# This function is like pretty good for now, doesn't need to be changed.
def connect2():
    import globalData as g
    valid = False
    while not valid:
        direction = random.randint(0,7)
        dlist = [(0,1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
        x = random.randint(0,14)
        y = random.randint(0,14)
        if g.boardPositions[y][x] == g.botColor:
            y += dlist[direction][1]
            x += dlist[direction][0]
            if g.boardPositions[y][x] == 0:
                return (x, y)
    return None