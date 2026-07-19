import pygame
import globals as g
import offlineMultiplayer as m

from mainMenu import mainMenu

pygame.init()
g.screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Gomuku Swap2")
g.img = pygame.image.load("assets/gomuku-swap2icon.bmp")
pygame.display.set_icon(g.img) 
g.clock = pygame.time.Clock()
g.running = True 

g.mode = 0

while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
    if g.mode == 0:
        mainMenu()
    elif g.mode == 1: # Multiplayer
        m.gameloop()
    elif g.mode == 2: # Singleplayer
        pass
    elif g.mode == 3:
        pass

    try:
        pygame.display.flip()
    except:
        break
pygame.quit()