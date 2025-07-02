"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

list_x = [3, 6, 9]
list_y = [6, 12, 18]
list_z = list_x + list_y  # union
list_x.extend(list_y)  # method -> void
print([((((value / 6) + (value / 3)) * 9) / 9) + value for value in list_x])
