class Animal:
    def __init__(self, type_str):
        self.__type = type_str

    def __str__(self):
        mvmnts = []
        action = ["digger", "slither", "swimmer", "walker", "flyer"]
        for i in action:
            if i in dir(self):
                mvmnts.append(f"{i}s")
        return f"\n A {self.type} named {self.name.capitalize()} that {' and '.join([', '.join(mvmnts[:-1]),mvmnts[-1]] if len(mvmnts) > 2 else mvmnts)} \n"

    @property
    def type(self):
        return self.__type
