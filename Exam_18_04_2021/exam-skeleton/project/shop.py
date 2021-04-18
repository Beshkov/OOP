from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository
from project.deliveries.product import Product


class Shop:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        product = self.create_product(product_type, name)

        if self.check_if_product_in_products(product):
            raise ValueError(f'Product {product.name} already exists.')

        if product:
            self.product_repository.add(product)
            return f"Product {product.name} successfully added to inventory."

    def sell(self, customer_name, **kwargs):

        if not customer_name in [c.name for c in self.customer_repository.customers]:

            customer = self.create_customer(customer_name)
            self.customer_repository.add(customer)

        else:
            customer = self.customer_repository.find(customer_name)


        for product, value in kwargs.items():
            if str(product) in [p.name for p in self.product_repository.products]:

                prod = [p for p in self.product_repository.products if p.name == str(product)][0]
                if prod.quantity <= value:
                    prod_quality = prod.quantity
                    self.product_repository.products.remove(prod)
                else:
                    prod_quality = value
                    self.product_repository.decrease(prod, value)

                customer.products[str(product)] = prod_quality
        result = ''
        for product_name, product_quantity in customer.products.items():
            result + "\n".join(f"Left quantity of {product_name}: {product_quantity}")

    @staticmethod
    def create_product(product_type, name):
        if product_type == 'Drink':
            return Drink(name)

        if product_type == 'Food':
            return Food(name)

    def check_if_product_in_products(self, product):
        return product.name in [p.name for p in self.product_repository.products]

    # def customer_operator(self, customer_name):
    #     if self.customer_repository.find(customer_name) == 'None':
    #         c = Customer(customer_name)
    #


    @staticmethod
    def create_customer(customer_name):
        return Customer(customer_name)


# s = Shop()
# customer = Customer('Gosho')
# s.deliver('Food', 'apple')
# s.deliver('Drink', 'cola')
# s.customer_repository.add(customer)
# s.sell("Gosho")
# print(s.sell("Pesho", apple=10, cola=10))
#
