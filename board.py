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

    pygame.display.flip()

    if pygame.mouse.get_pressed(3)[0]:
        print(pygame.mouse.get_pos())

    clock.tick(60)