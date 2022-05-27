import os

def playerdircheck(__path__, ls):
    for i in ls:
        if os.path.exists(__path__ + i) == False:
            print(os.path.exists(__path__ + i))
            print("some path doesn't exist")
            os.mkdir(i)
            print("some dir was just created")
        else:
            print(i + " is here ;)")

def playerfilescheck(__path__, ls):
    for i in ls:
        try:
            with open(__path__ + i, "r") as file:
                file.close()
        except:
            with open(__path__ + i, "x") as file:
                file.close()