# Funções decoradoras e decoradoresMore actions
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

from typing import Callable, Any


def build_function(func: Callable) -> Callable:
    def inside_def(*args: Any, **kwargs: Any):
        print("Decorator")
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print(f"{result=}")
        return result

    return inside_def


def reversed_string(value: str) -> str:
    return value[::-1]


def is_string(param: str) -> bool | None:
    if not isinstance(param, str):
        raise TypeError("param have is a str")


reversed_value = reversed_string("João")
print(reversed_value)
