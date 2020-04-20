from movements import ISlither
from .animal import Animal

class Rattlesnake(Animal, ISlither):
    def __init__(self, name):
        Animal.__init__(self, "timber rattlesnake")
        self.name = name
