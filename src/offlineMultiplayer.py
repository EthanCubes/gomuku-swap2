from win import *
import globalData as gD
import board as b

def game_loop():
    b.user_place_stone()
    b.render()
    calculate_win()
    gD.clock.tick(30)