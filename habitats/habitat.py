
class Habitat:
    def __init__(self, name, type_str):
        self.animals = []
        self.__type = type_str
        self.name = name

    @property
    def type(self):
        return self.__item

    def add_animal(self, *args):
        self.animals.extend([i for i in args])

    def __str__(self):
        animals = set([i.type for i in self.animals])
        animal_dict = dict()
        for animal in animals:
            animal_dict[f"{animal}"] = []
        for i in self.animals:
            animal_dict[f"{i.type}"].append(i.name.capitalize())
        final_sentence = [f"{a.capitalize()}s ({' and '.join([', '.join(v[:-1]),v[-1]] if len(v) > 2 else v)})" for a in animals for k,
                       v in animal_dict.items() if k == a]

        animal_str = ' and '.join([', '.join(
            final_sentence[:-1]), final_sentence[-1]] if len(final_sentence) > 2 else final_sentence)

        return f"\n This container holds a category of animals: {self.__type} : and is called {self.name} and has the following animals in it: {animal_str} \n \n"
