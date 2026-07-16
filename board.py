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
    global boardPositions
    boardPositions[yPos][xPos] = player

res = 45 # Change this according to screen resolution

pygame.init()
screen = pygame.display.set_mode((res*16, res*16))
pygame.display.set_caption("Gomuku Swap2")
img = pygame.image.load("gomuku-swap2icon.bmp")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
running = True

currentPlayer = 1
while running:
    currentPlayer *= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("peru")

    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (res, res+i*res), (res*15, res+i*res), round(res/12))
    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (res+i*res, res), (res+i*res, res*15), round(res/12))

    pygame.display.flip()

    xPos = res
    yPos = res
    for x in range(15):
        for y in range(15):
            if currentPlayer == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.circle(screen, color, (xPos, yPos), res/2)
            xPos += res
        yPos += res

    if pygame.mouse.get_pressed(3)[0]:
        mousePos = pygame.mouse.get_pos()
        gridX = round(mousePos[0]/res)
        gridY = round(mousePos[1]/res)
        if boardPositions[gridY][gridX] == 0:
            placeStone(gridX, gridY, currentPlayer)

    clock.tick(60)