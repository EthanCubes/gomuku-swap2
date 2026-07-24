import pygame
import global_data as gD
import offline_multiplayer as oM
import singleplayer as s

import random

from main_menu import main_menu_loop

pygame.init()
gD.screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Gomuku Swap2")
gD.img = pygame.image.load("assets/gomuku-swap2icon.bmp")
pygame.display.set_icon(gD.img)
gD.clock = pygame.time.Clock()
gD.running = True

gD.mode = 0

while gD.running:
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
            gD.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gD.mode = 0
                gD.reset_board()
    if gD.mode == 0:
        pygame.display.set_caption("Gomuku Swap2")
        main_menu_loop()
    elif gD.mode == 1: # Multiplayer
        pygame.display.set_caption("Gomuku Swap2: Local Multiplayer game")
        oM.game_loop()
    elif gD.mode == 2: # Singleplayer
        if gD.starter == 0:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are black)")
        else:
            pygame.display.set_caption("Gomuku Swap2: Game vs Bot (You are white)")
        s.game_loop()

    pygame.display.flip()
pygame.quit()