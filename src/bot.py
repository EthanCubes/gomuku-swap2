import globals as g
from random import randint
import board as b
from time import sleep

def botPlaceStone():
    sleep(0.25)
    valid = False
    while not valid:
        pos1 = randint(0, 14)
        pos2 = randint(0, 14)
        if g.boardPositions[pos2][pos1] == 0:
            valid = True
    b.placeStone(pos1, pos2, g.currentPlayer)

def analyze():
    # check for unblocked 3 in a row to block
    # check for 4 in a row to block
    # check for ways to get 5 in a row in 1 turn
    # check for ways to get 4 in a row in 1 turn
    # check for ways to get unblocked 3 in a row in 1 turn
    # check for ways to make 2x2 square
    pass