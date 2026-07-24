from win import *
import globalData as g
import board as b

def gameloop():
    b.user_place_stone()
    b.render()
    calcWin()
    g.clock.tick(30)