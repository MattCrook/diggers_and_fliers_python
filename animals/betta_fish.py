from movements import ISwimming
from .animal import Animal

class BettaFish(Animal, ISwimming):
    def __init__(self, name):
        Animal.__init__(self, "betta fish")
        self.name = name
