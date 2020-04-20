from movements import IDiggers
from .animal import Animal

class Gerbil(Animal, IDiggers):
    def __init__(self, name):
        Animal.__init__(self, "gerbil")
        self.name = name
