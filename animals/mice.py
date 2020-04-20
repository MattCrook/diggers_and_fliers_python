from movements import IDiggers, IWalking
from .animal import Animal

class Mice(Animal, IDiggers, IWalking):
    def __init__(self, name):
        Animal.__init__(self, "mouse")
        self.name = name
