import pygame
from win import *

defaultBoardPositions = [
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

def gameloop():
    global running, boardPositions, screen, clock
    
    screen.fill("peru")

    if currentPlayer == -1:
        pygame.draw.circle(screen, (0, 0, 0), (697, 23), 5)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (697, 23), 5)
    
    pygame.draw.circle(screen, (0, 0, 0), (360, 360), 10)

    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (45, 45+i*45), (675, 45+i*45), round(45/12))
    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (45+i*45, 45), (45+i*45, 675), round(45/12))

    xPos = 45
    yPos = 45
    for y in range(15):
        yPos = 45 + 45*y
        for x in range(15):
            xPos = 45 + 45*x
            if boardPositions[y][x] == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            if boardPositions[y][x] != 0:
                pygame.draw.circle(screen, color, (xPos, yPos), 20)

    if pygame.mouse.get_pressed(3)[0]:
        mousePos = pygame.mouse.get_pos()
        gridX = round(mousePos[0]/45) - 1
        gridY = round(mousePos[1]/45) - 1
        if gridX > 14:
            gridX = 14
        if gridY > 14:
            gridY = 14
        if boardPositions[gridY][gridX] == 0:
            placeStone(gridX, gridY, currentPlayer)
    if calcWin() != 0:
        running = False
        print(calcWin())
    clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((720, 720))
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
    gameloop()
    try:
        pygame.display.flip()
    except:
        break
pygame.quit()