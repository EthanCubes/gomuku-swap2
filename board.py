boardPositions = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def placeStone(xPos, yPos, player):
    global boardPositions
    boardPositions[yPos][xPos] = player

running = True
currentPlayer = -1
while running:
    inputValid = False
    while not inputValid:
        try:
            xPos = int(input("Enter xPos"))
            yPos = int(input("Enter yPos"))
        except:
            print("Input invalid")
            break
        if xPos < 0 or xPos > 14:
            print("Invalid position")
            break
        if yPos < 0 or yPos > 14:
            print("Invalid position")
            break
        if boardPositions[yPos][xPos] != 0:
             print("Position occupied")
             break
        inputValid = True

    placeStone(xPos, yPos, currentPlayer)
    for i in range(15):
        print(boardPositions[i])

    currentPlayer *= -1