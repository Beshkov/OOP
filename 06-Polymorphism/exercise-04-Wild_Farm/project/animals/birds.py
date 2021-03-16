from project.animals.animal import Animal

class Bird(Animal):
    def __init__(self, name, weight, food_eaten, wing_size):
        super().__init__(name,weight,food_eaten)
        self.wing_size = wing_size

    def make_sound(self):
        pass

class Owl(Bird):
    GROWTH = 0.25
    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):
    GROWTH = 0.35
    def make_sound(self):
        return "Cluck"
