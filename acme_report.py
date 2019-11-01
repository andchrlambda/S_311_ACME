"""This module generates randome products and prints a summary of them."""

from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap,' '???']

# price and weight should range from 5 to 100 (integers)
# flammability should range from 0.0 to 2.5 (float)


def generate_products(num_products=30):
    """Generates a given number of products randomly
    and returns them as a list.
    """
    products = []
    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                        flammability=flammability))
    return products        


def inventory_report(products):
    """Takes a list of products and prints a summary."""
    names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0
    for product in products:
        names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: {}".format(len(names)))
    print("Average price: {}".format(total_price / len(products)))
    print("Average weight: {}".format(total_weight / len(products)))
    print("Average flammability:{}".format(
            total_flammability / len(products)))

    print("Following is useful starting code for acme_report.py:")


if __name__ == '__main__':
    inventory_report(generate_products())
