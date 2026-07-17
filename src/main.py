import pygame

res = 45

pygame.init()
screen = pygame.display.set_mode((res*16, res*16))
pygame.display.set_caption("Gomuku Swap2")
img = pygame.image.load("assets/gomuku-swap2icon.bmp")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
running = True

mode = "mainMenu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    try:
        pygame.display.flip()
    except:
        break
pygame.quit()