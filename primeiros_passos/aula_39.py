"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#        +01234
#        -54321
string = "ABCDE"  # 5 caracteres (len)
list_name = ["João", "Tobias", "Irene", "Guilherme"]
print(list_name, type(list_name))
print(bool(list_name))  # lista vazia [] -> False ou cheia [1, 2, 3, 4, 5] -> True
# print(list_name[0].upper())

list_name[0] = "João Gabriel"
print(list_name)
