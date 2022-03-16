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


def test_add():
    basket_1 = Basket()
    basket_1.add(Product('b', 30))
    assert 'add' == basket_1.add(Product('b', 30))


test_2 = [([Product('zxc', 993), Product('qwe', 7)], 'remove')]

@pytest.mark.parametrize('products, s', test_2)
def test_remove_basket(products, s):
    basket_2 = Basket()
    for p in products:
        basket_2.add(p)
        assert s == basket_2.remove(p)

