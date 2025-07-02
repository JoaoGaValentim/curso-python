"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

name = "João Gabriel Valentim Theodoro"  # Iterável
iterator = iter(name)  # __iter__()
# print(next(iterator))  # __next__()
numbers = range(0, 10, 2)

while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break
