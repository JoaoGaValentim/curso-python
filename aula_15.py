# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Métodos úteis:
# add, update, clear, discard
numbers_x = {1, 2, 3, 4, 5, 6}
numbers_y = {1, 22, 12, 14, 15, 226}
numbers_z = set()

numbers_z.add(1)
numbers_z.add(2)
numbers_z.add(3)
numbers_z.discard(1)
print(numbers_z)
