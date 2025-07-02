# map - para mapear dadosMore actions
from collections.abc import Iterable
from functools import partial


def print_iter(iterator: Iterable) -> None:
    print(*list(iterator), sep="\n")
    print()


products = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


def add_percent(value: float, percent: float) -> float:
    return round(value * percent, 2)


add_ten_percent = partial(add_percent, percent=1.1)

"""
new_products = [
    {**product, "preco": add_percent(product["preco"], 1.1)} for product in products
]
"""


def update_product_price(product: dict) -> dict:
    return {**product, "preco": add_ten_percent(product["preco"])}


new_products = map(update_product_price, products)
print_iter(new_products)

print(*map(lambda value: value * 3, [1, 2, 3, 4]))
