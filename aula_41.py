# Decoradores com parâmetros

from typing_extensions import Any, Callable


def decorator_factory(factor: float | int = 0):
    def function_factory(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result: Any = func(*args, **kwargs)
            return result * factor

        return wrapper

    return function_factory


@decorator_factory(10)
@decorator_factory(100)
def sum(*args) -> float | int:
    result: float | int = 0
    for arg in args:
        if isinstance(arg, (float, int)):
            result += arg
    return result


# print(sum(1, 2, 3, 4, 5))
print(sum(10, 2))
