from .habitat import Habitat
from movements import IDiggers


class IDirt(Habitat):
    def __init__(self, name):
        super().__init__(name, type_str="digger")
        self.name = name

    # # Duck typing check
    def add_digger_pythonic(self, animal):
        try:
            if animal.dig_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(
                f'{animal} can\'t dig, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_digger_type_check(self, animal):
        if isinstance(animal, IDiggers):
            self.animals.add(animal)
        else:
            print(
                f'{animal} can\'t dig, so please do not try to put it in the {self.name} habitat')
