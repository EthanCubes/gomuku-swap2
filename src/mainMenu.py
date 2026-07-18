import pygame
import globals as g

image = pygame.image.load("assets/playWFriends.bmp")

def mainMenu():
    g.screen.fill("peru")
    g.screen.blit(image, (g.res*8-50, g.res*8-20))
    buttonClicked = g.buttonClicked((g.res*8-50, g.res*8-20), (g.res*8+50, g.res*8+20))
    if buttonClicked:
        g.mode = "playing"