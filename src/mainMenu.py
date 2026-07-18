import pygame
import globals as g

title = pygame.image.load("assets/title.bmp")
multiplayer = pygame.image.load("assets/playWFriends.bmp")

def mainMenu():
    g.screen.fill("peru")

    g.screen.blit(title, (g.res*8-150, g.res*2-50))

    # "Multiplayer" button
    g.screen.blit(multiplayer, (g.res*8-50, g.res*8-20))
    buttonClicked = g.buttonClicked((g.res*8-50, g.res*8-20), (g.res*8+50, g.res*8+20))
    if buttonClicked:
        g.mode = 1