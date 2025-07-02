"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def get_graphic_coords(x=0, y=0):
    return (x, y)


# print(get_graphic_coords())
# print(get_graphic_coords(x=1, y=2))


def fx(x=0, y=0, z=0):
    return (2 * x - (2 * (x**2))), (y + 2 * (y**2)), (2 * z)


function_x = fx(-1, 2, 2)
function_derivate_x = fx(-1, 2, 2)

for x in function_x:
    for x_derivate in function_derivate_x:
        print((((x**2) + (x_derivate**2)) * x_derivate) - (x * x_derivate * (2 * x)))
