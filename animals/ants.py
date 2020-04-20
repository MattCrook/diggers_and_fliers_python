from movements import IDiggers, IWalking
from .animal import Animal

class Ant(Animal, IDiggers, IWalking):
    def __init__(self, name):
        Animal.__init__(self, "ant")
        self.name = name
