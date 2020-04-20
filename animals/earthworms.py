from movements import ISlither
from .animal import Animal

class EarthWorms(Animal, ISlither):
    def __init__(self, name):
        Animal.__init__(self, "earthworms")
        self.name = name
