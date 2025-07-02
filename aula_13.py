# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

from typing_extensions import Any


coords = [[100, 100], [200, 200]]

map_board: dict[str, Any] = {
    "x": 100,
    "y": 200,
}

map_board.update({"coords": coords})
map_board.update(location="Yellow Room", level=0)
map_board.update(entities=("virus", "smiller"))
print(map_board)
