import pygame
from win import *
import globals as g
from time import sleep
import board as b
from random import randint

def setup():
    g.starter = randint(0, 1) # 0 is bot, 1 is human
    if g.starter == 0:
        print("You are black")
    else:
        print("You are white")

def gameloop():
    if g.currentPlayer == 1:
        if g.starter == 0:
            pass # bot's turn
        else:
            b.userPlaceStone()
    else:
        if g.starter == 0:
            b.userPlaceStone()
        else:
            pass # bot's turn
    b.render()
    calcWin()
    g.clock.tick(60)