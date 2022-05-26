import os

def playerdircheck(__path__):
    if os.path.exists(__path__ + "data/PLAYER") == False:
        print(os.path.exists(__path__ + "data/PLAYER"))
        print("doesn't exist")
        os.mkdir("data/PLAYER/")
        print("player dirf was just created")
    else:
        print("player dir exist ;)")