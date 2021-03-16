from abc import  ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight, food_eaten):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass
