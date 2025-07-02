# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
# import random

# # numbers = [random.randint(5, 10) for _ in range(10)]
# # numbers.sort()

# # print(numbers)

peoples = [
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "João", "sobrenome": "Theodoro"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

order_by_name = lambda item: item["nome"]
order_by_lastname = lambda item: item["sobrenome"]

peoples.sort(key=order_by_name)
# peoples.sort(key=order_by_lastname)

print(peoples)
