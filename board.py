import pygame

boardPositions = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def placeStone(xPos, yPos, player):
    global boardPositions, currentPlayer
    boardPositions[yPos][xPos] = player
    currentPlayer *= -1

def scanPosition(basePos, pos1, pos2, pos3, pos4):
    global boardPositions
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
    global boardPositions
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
            else:
                return 0
            # NE
            pos1 = (x + 1, y + 1)
            pos2 = (x + 2, y + 2)
            pos3 = (x + 3, y + 3)
            pos4 = (x + 4, y + 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # E
            pos1 = (x + 1, y)
            pos2 = (x + 2, y)
            pos3 = (x + 3, y)
            pos4 = (x + 4, y)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # SE
            pos1 = (x + 1, y - 1)
            pos2 = (x + 2, y - 2)
            pos3 = (x + 3, y - 3)
            pos4 = (x + 4, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # S
            pos1 = (x, y - 1)
            pos2 = (x, y - 2)
            pos3 = (x, y - 3)
            pos4 = (x, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # Sw
            pos1 = (x - 1, y - 1)
            pos2 = (x - 2, y - 2)
            pos3 = (x - 3, y - 3)
            pos4 = (x - 4, y - 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # W
            pos1 = (x - 1, y)
            pos2 = (x - 2, y)
            pos3 = (x - 3, y)
            pos4 = (x - 4, y)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0
            # NW
            pos1 = (x - 1, y + 1)
            pos2 = (x - 2, y + 2)
            pos3 = (x - 3, y + 3)
            pos4 = (x - 4, y + 4)
            if scanPosition(currentPosition, pos1, pos2, pos3, pos4) == 1:
                return 1
            elif scanPosition(currentPosition, pos1, pos2, pos3, pos4) == -1:
                return -1
            else:
                return 0

res = 45 # Change this according to screen resolution

pygame.init()
screen = pygame.display.set_mode((res*16, res*16))
pygame.display.set_caption("Gomuku Swap2")
img = pygame.image.load("assets/gomuku-swap2icon.bmp")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
running = True

currentPlayer = -1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("peru")

    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (res, res+i*res), (res*15, res+i*res), round(res/12))
    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (res+i*res, res), (res+i*res, res*15), round(res/12))

    xPos = res
    yPos = res
    for y in range(15):
        yPos = res + res*y
        for x in range(15):
            xPos = res + res*x
            if boardPositions[y][x] == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            if boardPositions[y][x] != 0:
                pygame.draw.circle(screen, color, (xPos, yPos), 20)

    if pygame.mouse.get_pressed(3)[0]:
        mousePos = pygame.mouse.get_pos()
        gridX = round(mousePos[0]/res) - 1
        gridY = round(mousePos[1]/res) - 1
        if gridX > 14:
            gridX = 14
        if gridY > 14:
            gridY = 14
        if boardPositions[gridY][gridX] == 0:
            placeStone(gridX, gridY, currentPlayer)
    if calcWin() != 0:
        running = False
        print(calcWin())
    pygame.display.flip()
    clock.tick(60)