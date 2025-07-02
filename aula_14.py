# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {"Luiz", 1, 2, 3}  # com dados

numbers_x = {2, 3, 6, 9, (1,)}
numbers_y = {1, 22, 9}
numbers_z = {1, 300, 543, 72}

# print(type(numbers_z), numbers_z.difference(numbers_y))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# values = [3, 3, 3, 3, 6, 9]
# values_set = set(values)
# print(list(values_set))

for x in numbers_x:
    print(x)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
print(numbers_x | numbers_y)
# intersecção & (intersection) - Itens presentes em ambos
print(numbers_x & numbers_y)
# diferença - Itens presentes apenas no set da esquerda
print(numbers_x - numbers_y)
# diferença simétrica ^ - Itens que não estão em ambos
print(numbers_x ^ numbers_y)
