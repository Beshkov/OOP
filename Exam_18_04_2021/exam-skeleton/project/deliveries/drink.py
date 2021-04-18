from project.deliveries.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name=name, quantity=10)