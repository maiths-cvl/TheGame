class Entity:
    def __init__(self, level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence):
        self.level = level
        self.health = health
        self.maxhealth = maxhealth
        self.food = food
        self.maxfood = maxfood
        self.walkspeed = walkspeed
        self.attackDmg = attackDmg
        self.defence = defence

        self.life = True

    def update(self):
        if self.health <= 0:
            self.life = False
            #print("you died")
        if self.health > 0:
            self.life = True
            #print(str(self) + " is living")

    def attack(self, target):
        if type(target) == list:
            for i in target:
                if type(i) == Entity or type(i):
                    i.hit(self.attackDmg)
        elif type(target) == Entity or type(i):
            target.hit(self.attackDmg)

    def hit(self, damage):
        calc = damage / (1 + (self.defence / 10))
        self.health -= calc
