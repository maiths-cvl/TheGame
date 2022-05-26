import entities.entity
from objects.entities.entity import Entity

class Player(Entity):
    def __init__(self, inventory):
        self.inventory = inventory