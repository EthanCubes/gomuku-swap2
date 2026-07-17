import pygame
import globals as g

res = 45

pygame.init()
g.screen = pygame.display.set_mode((res*16, res*16))
pygame.display.set_caption("Gomuku Swap2")
g.img = pygame.image.load("assets/gomuku-swap2icon.bmp")
pygame.display.set_icon(g.img)
g.clock = pygame.time.Clock()
g.running = True 

mode = "mainMenu"

while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
    try:
        pygame.display.flip()
    except:
        break
pygame.quit()