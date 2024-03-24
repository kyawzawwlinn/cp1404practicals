from car import Car
import random


class UnreliableCar(Car):
    """A car that might not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than its reliability."""
        if random.uniform(0, 100) < self.reliability:
            # Only drive if the car is reliable this time
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
