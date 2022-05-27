import os
import sys

def allGameCheck(__path__, ls):
    for i in ls:
        if os.path.exists(__path__ + i) == False:
            print("game crashed because a file has been deleted while the game was running")
            sys.exit()