import pygame
import offlineMultiplayer as m
import globals as g

def placeStone(xPos, yPos, player):
    g.boardPositions[yPos][xPos] = player
    g.currentPlayer *= -1

def userPlaceStone():
    if pygame.mouse.get_pressed(3)[0]:
        mousePos = pygame.mouse.get_pos()
        gridX = round(mousePos[0]/45) - 1
        gridY = round(mousePos[1]/45) - 1
        if gridX > 14:
            gridX = 14
        if gridY > 14:
            gridY = 14
        if g.boardPositions[gridY][gridX] == 0:
            placeStone(gridX, gridY, g.currentPlayer)

def render():
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
            if g.boardPositions[y][x] == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            if g.boardPositions[y][x] != 0:
                pygame.draw.circle(g.screen, color, (xPos, yPos), 20)