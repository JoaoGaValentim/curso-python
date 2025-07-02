# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b


def factorial(*args: int) -> str:
    try:
        values = list(args)
        values_end_value = values[len(values) - 1]
        values_str = (str(value) for value in values)
        operation_sequence = " x ".join(values_str)
        operation_result = 1

        if values[0] != 0 and values_end_value != 0:
            for value in values:
                operation_result *= int(value)
            return f"{values_end_value}! = {operation_sequence} = {operation_result}"
        res: str = f"{1}! = {1} = {1}"
        return res
    except ValueError as e:
        raise ValueError(e, "Permitido somente valores numáricos inteiros.")
    except UnboundLocalError as e:
        raise UnboundLocalError(e, "Não posso acessar")
    except TypeError as e:
        raise TypeError(e, "Erro na tipagem")


print(factorial(1, 2, 3, 4, 5))
value = 1
