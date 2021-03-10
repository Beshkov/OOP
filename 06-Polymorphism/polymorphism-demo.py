from abc import ABC, abstractmethod
from  math import  pi
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError("Subclass must implement")
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         print("Bark!")
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         print("Meow!")
#
# cat = Cat("Willy")
# cat.sound()
# dog = Dog("Willy")
# dog.sound()
# animal = Animal("Willy")
# animal.sound()

# Problem 2
# class Solution:
# class Shape(ABC):
#
#     @abstractmethod
#     def calculate_area(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         raise NotImplementedError
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return pi * (self.radius ** 2)
#
#     def calculate_perimeter(self):
#         return 2 * pi * self.radius
#
# class Rectangle(Shape):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def calculate_area(self):
#         return self.height * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)
#
# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
#
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
#


"""Problem 3: Execute - duck typing """

#
# def execute(func, *args):
#     return func(*args)
#
# def say_hello(name,my_name):
#     print(f"Hello, {name}, I am {my_name}")
#
# def say_bye(name):
#     print(f"Bye, {name}")
#
# execute(say_hello, "Peter", "George")
# execute(say_bye, "Peter")

# def play_instrument(func):
#     return func.play()
#
# class Guitar:
#     def play(self):
#         print("playing the guitar")
#
# guitar = Guitar()
# play_instrument(guitar)
#
# class Piano:
#     def play(self):
#         print("playing the piano")
# piano = Piano()
# play_instrument(piano)
