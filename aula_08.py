"""
Closure e funções que retornam outras funções
"""


def calculate(*args):
    def calculate_complex():
        complex_value = 0
        for value in args:
            if type(value) is not int:
                return 0
            complex_value += value
            complex_value **= value
        return complex_value

    return calculate_complex


for value in [10, 20, 30]:
    value = calculate(value)
    print(value())
