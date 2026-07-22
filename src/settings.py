import globalData as g

def settingsLoop():
    scaleMultiplier = 1
    backgroundColor = (205,133,63)
    boardColor = (0,0,0)
    musicVolume = 1
    try:
        data = None
        with open("~/.gomuku-options.txt") as f:
            data = f.read()
        dataList = data.split("\n")
        scaleMultiplier = dataList[0]
        backgroundColor = dataList[1]
        boardColor = dataList[2]
        musicVolume = dataList[3]
    except:
        scaleMultiplier = 1
        backgroundColor = (205,133,63)
        boardColor = (0,0,0)
        musicVolume = 1
    '''
    scaleMultiplier
    backgroundColor
    boardColor
    musicVolume
    '''
    with open("gomuku-options.txt", "w") as f:
        f.write("scaleMultiplier:"+str(scaleMultiplier))
        f.write("\nbackgroundColor:"+str(backgroundColor))
        f.write("\nboardColor:"+str(boardColor))
        f.write("\nmusicVolume:"+str(musicVolume))