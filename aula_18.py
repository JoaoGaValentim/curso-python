# Empacotamento e desempacotamento de dicionários
value_x, value_y = 12, 15
value_y, value_x = value_x, value_y
print(value_x, value_y)

people = {
    "name": "João",
    "age": 24,
}

locations = {
    "lat": -344354.2,
    "lon": -123345.3,
}

(name, name_v), (age, age_v) = people.items()
print(name, name_v)
print(age, age_v)

# unpack
people = {**people, **locations}

# print(people)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def get_dict_args(*args, **kwargs):
    return kwargs


# print(get_dict_args(**people))

commands = {
    "save": True,
    "reset": True,
}

print(get_dict_args(**commands))
