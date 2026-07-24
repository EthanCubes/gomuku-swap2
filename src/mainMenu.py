import pygame
import globalData as g
import board as b
from time import sleep
import singleplayer as s

title = pygame.image.load("assets/title.bmp")
singleplayer = pygame.image.load("assets/playWithBot.bmp")
multiplayer = pygame.image.load("assets/playWFriends.bmp")
quit = pygame.image.load("assets/quit.bmp")

def mainMenu():
    g.screen.fill("peru")

    g.screen.blit(title, (210, 90))

    # "Singleplayer" button
    g.screen.blit(singleplayer, (210, 270))
    buttonClicked = g.buttonClicked((210, 270), (300, 100))
    if buttonClicked:
        pygame.mixer.music.stop()
        g.currentPlayer = 1
        s.setup()
        g.mode = 2
        b.generate_start_pos()
        sleep(0.5)

    # "Multiplayer" button
    g.screen.blit(multiplayer, (210, 370))
    buttonClicked = g.buttonClicked((210, 370), (300, 100))
    if buttonClicked:
        pygame.mixer.music.stop()
        b.generate_start_pos()
        g.currentPlayer = 1
        g.mode = 1
        sleep(0.5)

    # Quit game button
    g.screen.blit(quit, (210, 470))
    buttonClicked = g.buttonClicked((210, 470), (300, 80))
    if buttonClicked:
        pygame.mixer.music.stop()
        g.running = False