"""
Tipo tupla - Uma lista imutável
"""

names = ("João", "Scooby", "Luna")  # tuple
# names[0] = "A" TypeError: 'tuple' object does not support item assignment
print(names[-1])

numbers_list = [2, 4, 8, 16, 32]
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
