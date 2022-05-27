def writeIn(path, content):
    with open(path, "a+") as file:
        file.write("\n")
        for i in content:
            file.write(i + "\n")
        file.close()