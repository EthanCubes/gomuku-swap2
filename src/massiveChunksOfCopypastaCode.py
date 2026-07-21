# 4 in a row scan
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
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (currentPosition,1)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (currentPosition,-1)
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            if scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == 1:
                return (1,currentPosition,pos1,pos2,pos3)
            elif scanPosition4(currentPosition, pos1, pos2, pos3, boardPosition) == -1:
                return (-1,currentPosition,pos1,pos2,pos3)
    return (None,0)