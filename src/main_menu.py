import pygame

import global_data
import global_data as gD
import board as b
from time import sleep
import singleplayer as s

title = pygame.image.load(gD.PROJECT_ROOT / "assets" / "title.bmp")
singleplayer = pygame.image.load(gD.PROJECT_ROOT / "assets" / "playWithBot.bmp")
multiplayer = pygame.image.load(gD.PROJECT_ROOT / "assets" / "playWFriends.bmp")
quit_button = pygame.image.load(gD.PROJECT_ROOT / "assets" / "quit.bmp")

def main_menu_loop():
    gD.screen.fill("peru")

    gD.screen.blit(title, (210, 90))

    # "Singleplayer" button
    gD.screen.blit(singleplayer, (210, 270))
    button_clicked = gD.button_clicked((210, 270), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        gD.currentPlayer = 1
        s.setup()
        gD.mode = 2
        b.generate_start_pos()
        sleep(0.5)

    # "Multiplayer" button
    gD.screen.blit(multiplayer, (210, 370))
    button_clicked = gD.button_clicked((210, 370), (300, 100))
    if button_clicked:
        pygame.mixer.music.stop()
        b.generate_start_pos()
        gD.currentPlayer = 1
        gD.mode = 1
        sleep(0.5)

    # Quit game button
    gD.screen.blit(quit_button, (210, 470))
    button_clicked = gD.button_clicked((210, 470), (300, 80))
    if button_clicked:
        pygame.mixer.music.stop()
        gD.running = False