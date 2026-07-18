import pygame
import globals as g

image = pygame.image.load("assets/playWFriends.bmp")

def mainMenu():
    g.screen.fill("peru")
    g.screen.blit(image, (g.res*8, g.res*8))
    buttonClicked = g.buttonClicked((g.res*6, g.res*7), (g.res*4, g.res*2))
    if buttonClicked:
        g.mode = "playing"