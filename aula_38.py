# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


# def concat_strings(value):
#     string_value = value

#     def pipe_concat(pipe_string):
#         nonlocal string_value
#         string_value += pipe_string
#         return string_value

#     return pipe_concat


# value = concat_strings("1")
# print(value("2"))
# print(value("3"))

from collections.abc import Callable


def add_more(value: float) -> Callable:
    aux_sum = value

    def inside_sum(inside_value: float) -> int | float:
        nonlocal aux_sum
        aux_sum += inside_value
        return aux_sum

    return inside_sum


add_to_result = add_more(10)

for i in range(100):
    print(add_to_result(i * 10))
