import pygame
from win import *
import globals as g
from time import sleep
import board as b

def gameloop():
    b.userPlaceStone()
    b.render()
    calcWin()
    g.clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                g.mode = 0
                g.resetBoard()