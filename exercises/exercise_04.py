"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

import random

classrooms_students_age = [
    [random.randint(5, 10) for _ in range(10)] for _ in range(10)
]


def search_duplicate(list_numbers):
    duplicate = -1
    for number in list_numbers:
        is_duplicate = list_numbers.count(number) > 1
        if is_duplicate:
            duplicate = number
            break

    return duplicate


duplicate_ages = set()
for index, classroom_ages in enumerate(classrooms_students_age, start=1):
    print(
        f"Sala {index} => {classroom_ages}",
        search_duplicate(classroom_ages),
    )
    duplicate_ages.add(search_duplicate(classroom_ages))
