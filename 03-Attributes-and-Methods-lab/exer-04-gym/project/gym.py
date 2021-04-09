class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer = [customer for customer in self.customers if subscription.id == customer.id][0]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription.id][0]
        equipment = [equip for equip in self.equipment if equip.id == subscription.id][0]
        plan = [plan for plan in self.plans if plan.id == subscription.id][0]
        return '\n'.join([str(x) for x in [subscription, customer, trainer, equipment, plan]])
