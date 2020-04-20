from movements import ISlither
from .animal import Animal

class CopperHead(Animal, ISlither):
    def __init__(self, name):
        Animal.__init__(self, "copperhead snake")
        self.name = name
