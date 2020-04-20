from movements import IFlyers
from .animal import Animal

class Finch(Animal, IFlyers):
    def __init__(self, name):
        Animal.__init__(self, "finch")
        self.name = name
