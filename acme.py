import random
from random import randint


class Product:
    """Creating class for ACME products."""

    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        """Establishing default values for ACME Product class"""
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """
        This method determines how stealable a Product is
        by dividing its price by its weight.
        """
        stealable = self.price / self.weight
        if stealable < 0.5:
            return "Not so stealable..."
        elif 1 > stealable >= 0.5:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """This method tests a Product's propensity to explode
        by muliplying its weight by its flammability.
        """
        exp = self.weight * self.flammability
        if exp < 10:
            return "...fizzle"
        elif 50 > exp >= 10:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Boxing Glove is a subclass of the ACME class Product
    with a different default weight.
    """
    def __init__(self, name=None, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """This Subclass method overrides the Class method
        for explode since boxing gloves do not explode.
        """
        return "... it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 15 > self.weight >= 5:
            return "Hey that hurt!"
        else:
            return "OUCH!"
