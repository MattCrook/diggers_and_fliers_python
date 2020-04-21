from .habitat import Habitat
from movements import IWalking


class IGrassy(Habitat):

    def __init__(self, name):
        super().__init__(name, type_str="walker")
        self.name = name

    # # Duck typing check
    def add_walker_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(
                f'{animal} can\'t walk, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_walker_type_check(self, animal):
        if isinstance(animal, IWalking):
            self.animals.add(animal)
        else:
            print(
                f'{animal} can\'t walk, so please do not try to put it in the {self.name} habitat')
