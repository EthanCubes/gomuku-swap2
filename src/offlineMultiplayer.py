from win import *
import globalData as gD
import board as b

def game_loop():
    b.user_place_stone()
    b.render()
    calcWin()
    gD.clock.tick(30)