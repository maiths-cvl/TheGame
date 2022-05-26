from main import *
import os

def playerdircheck():
    if os.path.exists(DATADIR) == False:
        print(os.path.exists(DATADIR))
        print("doesn't exist")
        os.mkdir("data/PLAYER/")
        print("player dirf was just created")
    else:
        print("player dir exist ;)")