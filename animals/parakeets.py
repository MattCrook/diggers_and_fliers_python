from movements import IFlyers, IWalking
from .animal import Animal

class Parakeet(Animal, IFlyers, IWalking):
    def __init__(self, name):
        Animal.__init__(self, "parakeet")
        self.name = name
