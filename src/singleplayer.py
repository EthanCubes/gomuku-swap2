import pygame
from win import *
import globalData as g
from time import sleep
import board as b
from random import randint
import bot

def setup():
    g.starter = randint(0, 1) # 0 is bot, 1 is human
    if g.starter == 0:
        g.botColor = 1
        g.playerColor = -1
    else:
        g.botColor = -1
        g.playerColor = 1

def gameloop():
    if g.currentPlayer == 1:
        if g.starter == 0:
            bot.botPlaceStone()
        else:
            b.userPlaceStone()
    else:
        if g.starter == 0:
            b.userPlaceStone()
        else:
            bot.botPlaceStone()
    b.render()
    calcWin()
    g.clock.tick(60)