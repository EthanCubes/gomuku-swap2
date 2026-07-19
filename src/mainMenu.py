import pygame
import globals as g
from time import sleep

title = pygame.image.load("assets/title.bmp")
singleplayer = pygame.image.load("assets/playWithBot.bmp")
multiplayer = pygame.image.load("assets/playWFriends.bmp")
settings = pygame.image.load("assets/settings.bmp")
quit = pygame.image.load("assets/quit.bmp")

def mainMenu():
    g.screen.fill("peru")

    g.screen.blit(title, (210, 90))

    # "Singleplayer" button
    g.screen.blit(singleplayer, (210, 270))
    buttonClicked = g.buttonClicked((210, 270), (300, 100))
    if buttonClicked:
        g.mode = 2

    # "Multiplayer" button
    g.screen.blit(multiplayer, (210, 370))
    buttonClicked = g.buttonClicked((210, 370), (300, 100))
    if buttonClicked:
        sleep(0.5)
        g.currentPlayer = -1
        g.mode = 1
    
    # Settings button
    g.screen.blit(settings, (210, 470))
    buttonClicked = g.buttonClicked((210, 470), (140, 40))
    if buttonClicked:
        g.mode = 3

    # Quit game button
    g.screen.blit(quit, (370, 470))
    buttonClicked = g.buttonClicked((370, 470), (140, 40))
    if buttonClicked:
        g.running = False