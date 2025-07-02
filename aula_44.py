from itertools import groupby

students = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Letícia", "nota": "B"},
    {"nome": "Fabrício", "nota": "A"},
    {"nome": "Rosemary", "nota": "C"},
    {"nome": "Joana", "nota": "D"},
    {"nome": "João", "nota": "A"},
    {"nome": "Eduardo", "nota": "B"},
    {"nome": "André", "nota": "A"},
    {"nome": "Anderson", "nota": "C"},
]


def order_by_name(student: dict) -> str:
    return student["nota"]


students_sorted = sorted(students, key=order_by_name)


groups = groupby(students_sorted, key=order_by_name)

for key, group in groups:
    for student in group:
        print(student)
