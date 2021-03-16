from project.animals.animal import Animal

class Mammal(Animal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name,weight,food_eaten)
        self.living_region = living_region

    def make_sound(self):
        pass

class Mouse(Mammal):
    GROWTH = 0.10
    def make_sound(self):
        return "Squeak"

class Dog(Mammal):
    GROWTH = 0.40
    LIKE_FOODS = "Meat"
    def make_sound(self):
        return "Woof!"

class Cat(Mammal):
    GROWTH = 0.30
    LIKE_FOODS = "Meat",
    def make_sound(self):
        return "Meow"

class Tiger(Mammal):
    GROWTH = 1.00
    LIKE_FOODS = "Meat"
    def make_sound(self):
        return "ROAR!!!"
