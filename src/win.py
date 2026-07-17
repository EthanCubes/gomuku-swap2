def scanPosition(basePos, pos1, pos2, pos3, pos4):
    from board import boardPositions
    basePosStatus = boardPositions[basePos[1]][basePos[0]]
    if basePosStatus == 0:
        return 0
    pos1Status = boardPositions[pos1[1]][pos1[0]]
    pos2Status = boardPositions[pos2[1]][pos2[0]]
    pos3Status = boardPositions[pos3[1]][pos3[0]]
    pos4Status = boardPositions[pos4[1]][pos4[0]]
    if basePosStatus == pos1Status:
        if basePosStatus == pos2Status:
            if basePosStatus == pos3Status:
                if basePosStatus == pos4Status:
                    return basePosStatus
    return 0

def calcWin():
    from board import boardPositions
    for y in range(4, 11):
        for x in range(4, 11):
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
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            pos4 = (x + 4, y + 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            pos4 = (x + 4, y)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            pos4 = (x + 4, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            pos4 = (x, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            pos4 = (x - 4, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            pos4 = (x - 4, y)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            pos4 = (x - 4, y + 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
    return 0   