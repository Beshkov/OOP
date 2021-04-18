from project.deliveries.product import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name=name, quantity=15)

