from .habitat import Habitat
from movements import IFlyers


class ICage(Habitat):

    def __init__(self, name):
        super().__init__(name, type_str="fly")
        self.name = name

    # Duck typing check
    def add_flyer_pythonic(self, animal):
        try:
            if animal.fly_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(
                f'{animal} can\'t fly, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_flyer_type_check(self, animal):
        if isinstance(animal, IFlyers):
            self.animals.add(animal)
        else:
            print(
                f'{animal} can\'t fly, so please do not try to put it in the {self.name} habitat')
