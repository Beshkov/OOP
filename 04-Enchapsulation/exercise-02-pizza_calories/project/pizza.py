from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}  # key -> topping type : value -> weight
        self.__toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, topping):
        self.__toppings = topping

    def add_topping(self, topping):
        if not len(self.toppings) + 1 < self.toppings_capacity:
            raise ValueError('Not enough space for another topping')
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return int(self.dough.weight) + sum(topping for topping in self.toppings.values())

