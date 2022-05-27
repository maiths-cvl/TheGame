from objects.entities.entity import Entity

class Player(Entity):
    def __init__(self, name, level, inventory, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence):
        super().__init__(level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence)
        self.name = name
        self.inventory = inventory

    def inv(self, stuff):
        if type(stuff) != list:
            print('here bro')
            return

        f = open('data/PLAYER/inventory/inventory.cfg', 'w+')
        if "[inventory]\n" in f.read():
            print("inventory ready")
        else:
            f.write("[inventory]\n")
            print("inventory was just initialized")

        num = 1
        for i in stuff:
            print(i)
            with open('data/PLAYER/inventory/inventory.cfg', 'a+') as file:
                file.write("\n" + str(num) +  " = " + str(i))
                num += 1