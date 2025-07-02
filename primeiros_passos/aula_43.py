"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# name = "João"
# copy_name = name
# name = "João Gabriel"
# print(name, copy_name)
list_x = [3, 6, 9, 1, 2, 3, 6, 12, 18]
list_y = list_x.copy()  # pointer
list_y.append(9)
print(list_y)
