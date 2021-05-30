import random
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, {}% unreliable".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if random.randint(0, 100) < int(self.reliability):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
