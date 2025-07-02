# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b
from functools import reduce


def factorial(*args):
    try:
        numbers = list(args)
        calculate_factorial = lambda start, end: int(start * end)
        result_factorial = reduce(calculate_factorial, numbers)
        return result_factorial or 1
    except (ValueError, UnboundLocalError) as e:
        raise Exception(e, "Permitido somente valores numáricos inteiros.")
    except TypeError as e:
        raise TypeError(e, "Erro na tipagem")


n = 5
values = (value + 1 for value in range(n))
factorial_result = factorial(*values)
sequence = []
for i in range(n):
    sequence.append(str((i % n) + 1))

print(n, "!=", " x ".join(sequence), "=", factorial_result)
