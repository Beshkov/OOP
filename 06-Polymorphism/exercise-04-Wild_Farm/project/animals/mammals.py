from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    GROWTH = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(Mouse.GROWTH, food)

class Dog(Mammal):
    GROWTH = 0.40
    LIKE_FOODS = "Meat"

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(Dog.GROWTH, food)

class Cat(Mammal):
    GROWTH = 0.30
    LIKE_FOODS = "Meat",

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(Cat.GROWTH, food)

class Tiger(Mammal):
    GROWTH = 1.00
    LIKE_FOODS = "Meat"

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"


    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(Tiger.GROWTH, food)


mice = Mouse("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(mice)
print(mice.make_sound())
print(mice.feed(veg))
print(mice.feed(fruit))
print(mice.feed(meat))
print(mice)
