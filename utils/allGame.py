import os
import sys

def allGameCheck(__path__):
    if os.path.exists(__path__ + "data/PLAYER") == False:
        print("game crashed because a file has been deleted while the game was running")
        sys.exit()