from main import Product, Basket
import pytest

tests = [([Product('a', 50), Product('b', 30)], 80)]


@pytest.mark.parametrize('products, s', tests)
def test_basket(products, s):
    basket = Basket()
    for p in products:
        basket.add(p)
    assert s == basket.count_sum()


def test_name():
    product = Product('name', 10)
    assert product.name == 'name'


def test_price():
    product = Product('name', 10)
    assert product.price == 10

a = Product('a', 50)
b = Product('b', 30)

def test_add():
    basket3 = Basket([a])
    basket4 = Basket([a, b])
    basket3.add(b)
    assert basket3.basket == basket4.basket

    # pr.name for pr in self.basket
def test_remove():
    basket = Basket([a, b])
    basket2 = Basket([a])
    basket.remove(b)
    assert basket2.basket == basket.basket

# test_2 = [([Product('zxc', 993), Product('qwe', 7)], 'remove')]
#
# @pytest.mark.parametrize('products, s', test_2)
# def test_remove_basket(products, s):
#     basket_2 = Basket()
#     for p in products:
#         basket_2.add(p)
#         assert s == basket_2.remove(p)
