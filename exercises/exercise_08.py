# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


from itertools import zip_longest

cities = ["Salvador", "Ubatuba", "Belo Horizonte"]
states = ["BA", "SP", "MG", "RJ"]


# def zipper(cities=[], states=[]):
#     interval = min(len(cities), len(states))
#     return [(cities[i], states[i]) for i in range(interval)]


# print(zipper(cities, states))

print(list(zip_longest(cities, states, fillvalue="SEM CIDADE")))
