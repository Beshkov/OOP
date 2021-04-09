class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.name = name
        self.endurance = endurance
        self.sprint = sprint
        self.dribble = dribble
        self.passing = passing
        self.shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, endurance):
        self.__endurance = endurance

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, sprint):
        self.__sprint = sprint

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, dribble):
        self.__dribble = dribble

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, passing):
        self.__passing = passing

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, shooting):
        self.__shooting = shooting

    def __str__(self):
        return f'Player: {self.name}\n' \
               f'Endurance: {self.endurance}\n' \
               f'Sprint: {self.sprint}\n' \
               f'Dribble: {self.dribble}\n' \
               f'Passing: {self.passing}\n' \
               f'Shooting: {self.shooting}\n'
