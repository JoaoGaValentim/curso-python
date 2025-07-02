# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10, 100, 2)))
import pprint

products = [
    {
        "name": "Leite De Soja",
        "price": 35,
    },
    {
        "name": "Leite",
        "price": 40,
    },
    {
        "name": "Leite",
        "price": 11,
    },
    {
        "name": "Laranja",
        "price": 50,
    },
]

print_dict = lambda list_dict: pprint.pprint(list_dict, sort_dicts=False, width=98)

map_product = [
    (
        {
            **product,
            "name": product["name"],
            "price": product["price"] * 1.05,
        }
        if product["price"] > 10
        else {**product}
    )
    for product in products
]

print_dict(map_product)

filter_product = [
    (
        {
            **product,
            "name": product["name"],
            "price": product["price"] * 1.05,
        }
        if product["price"] > 10
        else {**product}
    )
    for product in products
    if product["price"] >= 20 and product["price"] * 1.05 > 10
]

print_dict(filter_product)
