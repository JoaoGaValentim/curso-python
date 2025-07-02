# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

people = {
    "id": 1,
    "first_name": "João Gabriel Valentim",
    "last_name": "Theodoro",
    "age": 24,
    "profission": "developer",
    "location": [1000, 1000, 1000],
}

people_copy = copy.deepcopy(people)
people_copy["location"] = [1000, 1000, "Óleo"]
people_copy["location"][1] = 2
print(people, people_copy)
