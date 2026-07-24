import pygame
import globalData as g
import offlineMultiplayer as m
import singleplayer as s

import random

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
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.unload()
        number = random.randint(1,3)
        if number == 1:
            pygame.mixer.music.load("assets/music/amazingPlan.mp3")
        elif number == 2:
            pygame.mixer.music.load("assets/music/elevatorMusic.mp3")
        else:
            pygame.mixer.music.load("assets/music/schemingWeaselFaster.mp3")
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                g.mode = 0
                g.resetBoard()
    if g.mode == 0:
        pygame.display.set_caption("Gomuku Swap2")
        mainMenu()
    elif g.mode == 1: # Multiplayer
        pygame.display.set_caption("Gomuku Swap2: Local Multiplayer game")
        m.gameloop()
    elif g.mode == 2: # Singleplayer
        if g.starter == 0:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are black)")
        else:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are white)")
        s.gameloop()

    pygame.display.flip()
pygame.quit()