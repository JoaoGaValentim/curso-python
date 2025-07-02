"""
Lista de listas e seus índices
"""

classrooms = [
    ["João", "Clara"],
    ["Lucas", "Ana"],
    ["José", "Pedro", "Maria", (7, 8, 10)],
]

# print(classrooms[2][3][0])

for classroom in classrooms:
    print(f"A sala é {classroom}")
    for students in classroom:
        print(students)
