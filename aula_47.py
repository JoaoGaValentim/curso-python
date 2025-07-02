from functools import reduce

products = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

total_price = reduce(
    lambda accumulator, next_value: round(accumulator + next_value["preco"], 2),
    products,
    0,
)

print(total_price)
