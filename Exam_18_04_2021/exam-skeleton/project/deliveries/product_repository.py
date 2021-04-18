from project.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        if product.name in [p.name for p in self.products]:
            raise ValueError(f'Product {product.name} already exists.')

        self.products.append(product)
        return f'Product {product.name} successfully added to inventory.'

    def decrease(self, product: Product, quantity: int):
        product.quantity -= quantity
        return f'Left quantity of {product.name}: {product.quantity}'

    def find(self, product_name: str):
        product = [p for p in self.products if p.name == product_name]
        if product:
            return product[0]
        return 'None'

