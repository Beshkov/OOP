class MovieWorld:
    max_dvd_capacity = 15
    max_customer_capacity = 10
    def __init__(self, name):
        self.name = name
        self.customers = []  # list with Customers objects
        self.dvds = []  # list with DVDs objects

    @staticmethod
    def dvd_capacity():
        return MovieWorld.max_dvd_capacity

    @staticmethod
    def customer_capacity():
        return MovieWorld.max_customer_capacity

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        # for customer in self.customers:
        #     if customer_id == customer.id:
        #         for dvd in customer.rented_dvds:
        #             if dvd_id == dvd.id:
        #                 return f"{customer.name} has already rented {dvd.name}"
        #         for dvd in self.dvds:
        #             if dvd_id == dvd.id and dvd.is_rented:
        #                 return 'DVD is already rented'
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return 'DVD is already rented'
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"


    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f'{customer.__repr__()}\n'
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result



