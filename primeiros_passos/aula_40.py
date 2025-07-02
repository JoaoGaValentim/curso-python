"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#               0   1   2   3   4   5
from typing_extensions import Any


list_numbers: Any = [10, 20, 30, 40]
# number = list_numbers[2]
# print(number)
# list_numbers[2] = 60
# print(list_numbers[2])
# del list_numbers[2]
# print(list_numbers[2])
list_numbers.append(50)  # adicionar ao final
list_numbers.pop(3)  # removi o 50
list_numbers.append(60)
list_numbers.append("221B")
last_remove = list_numbers.pop()
print(list_numbers, last_remove)
