from typing import List


class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price

class Basket:
    basket: List[Product] = []

    def add(self, product):
        self.basket.append(product)
        return 'add'

    def remove(self, product):
        self.basket.remove(product)
        return 'remove'

    def count_sum(self):
        return sum([pr.price for pr in self.basket])
