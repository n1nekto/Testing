from typing import List


class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price

class Basket:
    def __init__(self, products=[]):
        self.basket: List[Product] = products

    # basket: List[Product] = []

    def add(self, product):
        self.basket.append(product)

    def remove(self, product):
        self.basket.remove(product)

    def count_sum(self):
        return sum([pr.price for pr in self.basket])
