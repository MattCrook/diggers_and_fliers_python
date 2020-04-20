from .habitat import Habitat
from movements import ISwimmers


class IAquarium(Habitat):

    def __init__(self, name):
        super().__init__(name, type_str="swimmer")
        self.name = name

    # Duck typing check
    # def add_swimmer_pythonic(self, animal):
    #     try:
    #         if animal.swim_speed > -1:
    #             self.animals.add(animal)
    #     except AttributeError as ex:
    #         print(
    #             f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # # Actual typing check
    # def add_swimmer_type_check(self, animal):
    #     if isinstance(animal, ISwimmers):
    #         self.animals.add(animal)
    #     else:
    #         print(
    #             f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')
