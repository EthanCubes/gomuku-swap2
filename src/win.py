import pygame
from time import sleep
import globalData as g
import board as b

def scanPosition(basePos, pos1, pos2, pos3, pos4, boardPosition):
    try:
        basePosStatus = boardPosition[basePos[1]][basePos[0]]
        if basePosStatus == 0:
            return 0
        pos1Status = boardPosition[pos1[1]][pos1[0]]
        pos2Status = boardPosition[pos2[1]][pos2[0]]
        pos3Status = boardPosition[pos3[1]][pos3[0]]
        pos4Status = boardPosition[pos4[1]][pos4[0]]
        if basePosStatus == pos1Status:
            if basePosStatus == pos2Status:
                if basePosStatus == pos3Status:
                    if basePosStatus == pos4Status:
                        return basePosStatus
    except:
        return 0
    return 0

def generateScan(boardPosition):
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
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (1, currentPosition, pos1, pos2, pos3, pos4)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (-1, currentPosition, pos1, pos2, pos3, pos4)
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            pos4 = (x + 4, y + 4)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            pos4 = (x + 4, y)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            pos4 = (x + 4, y - 4)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            pos4 = (x, y - 4)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            pos4 = (x - 4, y - 4)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            pos4 = (x - 4, y)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            pos4 = (x - 4, y + 4)
            if not (pos4[0] < 0 or pos4[0] > 14 or pos4[1] < 0 or pos4[1] > 14):
                valid = True
            else:
                valid = False
            g.winLine[0] = currentPosition
            g.winLine[1] = pos4
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == 1 and valid:
                return (currentPosition,1)
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4, boardPosition) == -1 and valid:
                return (currentPosition,-1)
    return (None,0)

def calcWin():
    if generateScan(g.boardPositions)[1] != 0:
        b.render()
        pygame.draw.line(g.screen, (255, 0, 0), (g.winLine[0][0]*45+45, g.winLine[0][1]*45+45), (g.winLine[1][0]*45+45, g.winLine[1][1]*45+45), 5)
        pygame.display.flip()
        if generateScan(g.boardPositions)[1] == 1:
            pygame.display.set_caption("Gomuku Swap2: White victory!")
        else:
            pygame.display.set_caption("Gomuku Swap2: Black Victory!")
        sleep(1)
        g.mode = 0
        g.resetBoard()
    placedStones = 0
    for y in range(15):
        for x in range(15):
            if g.boardPositions[y][x] != 0:
                placedStones += 1
    if placedStones == 225:
        b.render()
        pygame.display.flip()
        pygame.display.set_caption("Gomuku Swap2: Draw!")
        sleep(1)
        g.mode = 0
        g.resetBoard()