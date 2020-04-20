from movements import IDiggers, IWalking, ISwimming
from .animal import Animal

class Terrapins(Animal, IDiggers, IWalking, ISwimming):
    def __init__(self, name):
        Animal.__init__(self, "terrapin")
        self.name = name
