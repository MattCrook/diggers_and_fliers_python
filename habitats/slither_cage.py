from .habitat import Habitat
from movements import ISlither


class IAmazon(Habitat):
    def __init__(self, name):
        super().__init__(name, type_str="slither")
        self.name = name

    # Duck typing check
    def add_slither_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(
                f'{animal} can\'t slither, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_slither_type_check(self, animal):
        if isinstance(animal, ISlither):
            self.animals.add(animal)
        else:
            print(
                f'{animal} can\'t slither, so please do not try to put it in the {self.name} habitat')
