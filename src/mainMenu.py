import pygame
import globals as g

title = pygame.image.load("assets/title.bmp")
singleplayer = pygame.image.load("assets/playWithBot.bmp")
multiplayer = pygame.image.load("assets/playWFriends.bmp")
settings = pygame.image.load("assets/settings.bmp")
quit = pygame.image.load("assets/quit.bmp")

def mainMenu():
    g.screen.fill("peru")

    g.screen.blit(title, (g.res*8-150, g.res*2))

    # "Singleplayer" button
    g.screen.blit(singleplayer, (g.res*8-150, g.res*6))
    buttonClicked = g.buttonClicked((g.res*8-150, g.res*6-40), (g.res*8+150, g.res*6+40))
    if buttonClicked:
        g.mode = 2

    # "Multiplayer" button
    g.screen.blit(multiplayer, (g.res*8-150, g.res*8))
    buttonClicked = g.buttonClicked((g.res*8-150, g.res*8-40), (g.res*8+150, g.res*8+40))
    if buttonClicked:
        g.mode = 1
    
    # Settings button
    g.screen.blit(settings, (g.res*5-15, g. res*10))
    buttonClicked = g.buttonClicked((g.res*8-150, g.res*9), (g.res*8+150, g.res*9))
    if buttonClicked:
        g.mode = 3

    # Quit game button
    g.screen.blit(quit, (g.res*10-80, g. res*10))
    buttonClicked = g.buttonClicked((g.res*8-150, g.res*9-40), (g.res*8+150, g.res*9+40))