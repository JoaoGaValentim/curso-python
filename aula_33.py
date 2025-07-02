# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


def create_zero_exception(value):
    if value == 0:
        raise ZeroDivisionError("Erro de divisão por zero")
    return True


def division(dividend=1, divisor=1):
    create_zero_exception(divisor)
    return dividend / divisor


print(division(0, 0))
