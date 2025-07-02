# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

numbers_x = {1, 2, 3, 4, 5, 6}
numbers_y = {1, 22, 12, 14, 15, 226}

# Operadores úteis:
# união | união (union) - Une
print(numbers_x | numbers_y)
# intersecção & (intersection) - Itens presentes em ambos
print(numbers_x & numbers_y)
# diferença - Itens presentes apenas no set da esquerda
print(numbers_x - numbers_y)
# diferença simétrica ^ - Itens que não estão em ambos
print(numbers_x ^ numbers_y)
