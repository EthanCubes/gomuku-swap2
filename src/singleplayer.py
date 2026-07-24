from win import *
import globalData as gD
import board as b
from random import randint
import bot

def setup():
    gD.starter = randint(0, 1) # 0 is bot, 1 is human
    if gD.starter == 0:
        gD.botColor = 1
        gD.playerColor = -1
    else:
        gD.botColor = -1
        gD.playerColor = 1

def game_loop():
    if gD.currentPlayer == 1:
        if gD.starter == 0:
            bot.bot_place_stone()
        else:
            b.user_place_stone()
    else:
        if gD.starter == 0:
            b.user_place_stone()
        else:
            bot.bot_place_stone()
    b.render()
    calcWin()
    gD.clock.tick(30)