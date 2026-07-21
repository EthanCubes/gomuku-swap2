# 4 in a row scan. This is actually used to find 3 in a rows to block because yeah
def scanPosition4(basePos, pos1, pos2, pos3, boardPosition):
    try:
        basePosStatus = boardPosition[basePos[1]][basePos[0]]
        if basePosStatus == 0:
            return 0
        pos1Status = boardPosition[pos1[1]][pos1[0]]
        pos2Status = boardPosition[pos2[1]][pos2[0]]
        pos3Status = boardPosition[pos3[1]][pos3[0]]
        if basePosStatus == pos1Status:
            if basePosStatus == pos2Status:
                if basePosStatus == pos3Status:
                    return basePosStatus
    except:
        return 0
    return 0

def generateScan4(boardPosition):
    for y in range(15):
        for x in range(15):
            currentPosition = (x, y)
            pos1 = ()
            pos2 = ()
            pos3 = ()
            # N
            pos1 = (x, y + 1)
            pos2 = (x, y + 2)
            pos3 = (x, y + 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1, currentPosition, pos1, pos2, pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1, currentPosition, pos1, pos2, pos3)
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            if not (pos3[0] < 0 or pos3[0] > 14 or pos3[1] < 0 or pos3[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2,pos3)
    return (None,0)


# 3 in a row scan. This is actually used to find 2 in a rows to block because yeah
def scanPosition3(basePos, pos1, pos2, boardPosition):
    try:
        basePosStatus = boardPosition[basePos[1]][basePos[0]]
        if basePosStatus == 0:
            return 0
        pos1Status = boardPosition[pos1[1]][pos1[0]]
        pos2Status = boardPosition[pos2[1]][pos2[0]]
        if basePosStatus == pos1Status:
            if basePosStatus == pos2Status:
                return basePosStatus
    except:
        return 0
    return 0

def generateScan3(boardPosition):
    for y in range(15):
        for x in range(15):
            currentPosition = (x, y)
            pos1 = ()
            pos2 = ()
            # N
            pos1 = (x, y + 1)
            pos2 = (x, y + 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1, currentPosition, pos1, pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1, currentPosition, pos1, pos2)
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            if not (pos2[0] < 0 or pos2[0] > 14 or pos2[1] < 0 or pos2[1] > 14):
                valid = True
            else:
                valid = False
            if scanPosition3(currentPosition, pos1, pos2, boardPosition) == 1 and valid:
                return (1,currentPosition,pos1,pos2)
            elif scanPosition3(currentPosition, pos1, pos2, boardPosition) == -1 and valid:
                return (-1,currentPosition,pos1,pos2)
    return (None,0)