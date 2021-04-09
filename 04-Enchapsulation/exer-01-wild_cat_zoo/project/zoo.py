from .lion import Lion
from .tiger import Tiger
from .cheetah import Cheetah
from .keeper import Keeper
from .caretaker import Caretaker
from .vet import Vet


class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if not self.__budget - price < 0 and not self.__animal_capacity - (len(self.animals) + 1) < 0:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif self.__budget - price < 0:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity - (len(self.workers) + 1) < 0:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget - salaries < 0:
            return 'You have no budget to pay your workers. They are unhappy'
        self.__budget -= salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        animals_needs = sum([animal.get_needs() for animal in self.animals])
        if self.__budget - animals_needs < 0:
            return 'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= animals_needs
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join(str(l) for l in lions)
        result += f'\n----- {len(tigers)} Tigers:\n'
        result += '\n'.join(str(t) for t in tigers)
        result += f'\n----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join(str(c) for c in cheetahs)
        return result

    def workers_status(self):
        caretakers = [str(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        vet = [str(worker) for worker in self.workers if isinstance(worker, Vet)]
        keeper = [str(worker) for worker in self.workers if isinstance(worker, Keeper)]
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keeper)} Keepers:\n'
        result += '\n'.join(keeper)
        result += f'\n----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers)
        result += f'\n----- {len(vet)} Vets:\n'
        result += '\n'.join(vet)
        return result
