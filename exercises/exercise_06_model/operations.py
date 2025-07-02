import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

produtos_copia = [
    {**product, "preco": round(product["preco"] * 1.1, 2)}
    for product in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    produtos_copia, key=lambda p: p["nome"], reverse=True
)

produtos_ordenados_por_preco = sorted(
    produtos_copia,
    key=lambda p: p["preco"],
)
