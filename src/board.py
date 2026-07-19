import pygame
from win import *
import globals as g
from time import sleep

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
    global boardPositions
    boardPositions[yPos][xPos] = player
    g.currentPlayer *= -1

def gameloop():
    global running, boardPositions, screen, clock
    
    g.screen.fill("peru")
    if g.currentPlayer == -1:
        pygame.draw.circle(g.screen, (0, 0, 0), (697, 23), 5)
    else:
        pygame.draw.circle(g.screen, (255, 255, 255), (697, 23), 5)
    
    pygame.draw.circle(g.screen, (0, 0, 0), (360, 360), 10)

    for i in range(15):
        pygame.draw.line(g.screen, (0, 0, 0), (45, 45+i*45), (675, 45+i*45), round(45/12))
    for i in range(15):
        pygame.draw.line(g.screen, (0, 0, 0), (45+i*45, 45), (45+i*45, 675), round(45/12))

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
                pygame.draw.circle(g.screen, color, (xPos, yPos), 20)

    if pygame.mouse.get_pressed(3)[0]:
        mousePos = pygame.mouse.get_pos()
        gridX = round(mousePos[0]/45) - 1
        gridY = round(mousePos[1]/45) - 1
        if gridX > 14:
            gridX = 14
        if gridY > 14:
            gridY = 14
        if boardPositions[gridY][gridX] == 0:
            placeStone(gridX, gridY, g.currentPlayer)
    if calcWin() != 0:
        print(calcWin())
        sleep(1)
        g.mode = 0
    g.clock.tick(60)