# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o PythonMore actions
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

from typing import Any, Callable


def build_function(func: Callable) -> Callable:
    def inside_def(*args: Any, **kwargs: Any):
        print("Decorator")
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print(f"{result=}")
        print("Decorator started")
        return result

    return inside_def


@build_function
def reversed_string(value: str) -> str:
    print(reversed_string.__name__)
    return value[::-1]


def is_string(param: str) -> bool | None:
    if not isinstance(param, str):
        raise TypeError("param have is str")


reversed_value = reversed_string("123")
print(reversed_value)
