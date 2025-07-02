# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

loaction = dict(lat=1000, lon=233)
peoples = [
    {
        "id": 1,
        "first_name": "João Gabriel Valentim",
        "last_name": "Theodoro",
        "age": 24,
        "profission": "developer",
        "location": [loaction, "Óleo"],
    },
    {
        "id": 2,
        "first_name": "Guilherme Valentim",
        "last_name": "Theodoro",
        "age": 16,
        "profission": "student",
        "location": [loaction, "Óleo"],
    },
]

for _, people_dict in enumerate(peoples):
    for key in people_dict:
        print(people_dict[key])

for _, people_dict in enumerate(peoples):
    for key, value in people_dict.items():
        print(f"{key} => {value}")
