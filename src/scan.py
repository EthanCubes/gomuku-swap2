import random
import globalData as g

# This function is like pretty good for now, doesn't need to be changed.
def connect2():
    import globalData as g
    valid = False
    while not valid:
        direction = random.randint(0,7)
        dlist = [(0,1),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
        x = random.randint(0,14)
        y = random.randint(0,14)
        if g.boardPositions[y][x] == g.botColor:
            y += dlist[direction][1]
            x += dlist[direction][0]
            if g.boardPositions[y][x] == 0:
                return x, y
generateScan([0,0,0,0,0,0])