#Exercise 1
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        print(f"{self.make} {self.model} - Capacity: {self.capacity} tons")

    def wheels(self):
        return 6


car = Car("Toyota", "Corolla")
truck = Truck("Volvo", "FH16", 20)

car.describe()
truck.describe()

#Exercise 2
truck = Truck("Volvo", "FH16", 20)

#Exercise 3
def describe(self):
    print(f"{self.make} {self.model} - Capacity: {self.capacity} tons")

#Exercise 4
vehicles = [
    Car("Toyota", "Corolla"),
    Truck("Volvo", "FH16", 20),
    Car("Honda", "Civic"),
    Truck("Mercedes", "Actros", 18)
]

for vehicle in vehicles:
    vehicle.describe()

#Exercise 5
print(car.wheels())
print(truck.wheels())

