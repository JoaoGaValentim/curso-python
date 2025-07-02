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

people = {
    "id": 1,
    "first_name": "João Gabriel Valentim",
    "last_name": "Theodoro",
    "age": 24,
    "profission": "developer",
    "location": [1000, 1000, "Óleo"],
}

print(len(people))
print(people.keys())
print(people.values())
print(people.items())
people.setdefault("phone", "14999999999")
print(people)
print(people.get("phone"))
people.update({"first_name": "João"})
print(people)

people_copy = people.copy()
print(people_copy)
people_copy.pop("first_name")
people_copy.popitem()
print(people_copy)
print(people)

for key, value in people.items():
    print(f"{key}: {value}")
