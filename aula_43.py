# Combinations, Permutations e Product - ItertoolsMore actions
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from collections.abc import Iterator
from itertools import combinations, permutations, product

peoples = [
    "João",
    "Joana",
    "Luiz",
    "Letícia",
]

clothes = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculina", "feminina"],
    ["regata", "manga_longa"],
]


def print_iter(iterator: Iterator) -> None:
    print(*list(iterator), sep="\n")


print_iter(combinations(peoples, 2))
print_iter(permutations(peoples, 2))
print_iter(product(*clothes))
