products = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


def filter_product_more_if_one_houndred(product):
    return product["preco"] > 100


products_filter = filter(filter_product_more_if_one_houndred, products)
print(*products_filter)
