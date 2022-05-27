from objects.entities.entity import Entity

class Player(Entity):
    def __init__(self, name, level, slot, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence):
        super().__init__(level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence)
        self.name = name
        self.slot = slot
        self.inventory = self.readInv()


    def inv(self, stuff):
        self.inventory = stuff

        with open('data/PLAYER/inventory/inventory.txt', "w+") as file:
            for i in stuff:
                file.write(str(i) + ";")
            file.close()

    def readInv(self):
        with open('data/PLAYER/inventory/inventory.txt', "r+") as file:
            listof = file.read()
            listof = listof.split(';')
            listof.remove('')
            return listof