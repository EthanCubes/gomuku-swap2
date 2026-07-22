import globalData as g

def settingsLoop():
    try:
        with open("gomuku-options.txt") as f:
            print(f.read())
    except:
        pass
    '''
    scaleMultiplier
    backgroundColor
    boardColor
    musicVolume
    '''
    with open("gomuku-options.txt", "w") as f:
        f.write("Hello")