# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10, 100, 2)))

list_odd = []
# for number in range(100):
#     if number % 2 == 1:
#         list_odd.append(number)

print([number % 3 for number in range(100)])
