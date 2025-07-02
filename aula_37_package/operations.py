__all__ = ["name", "fibonacci", "collatz"]


name: str = "Joao"


def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def collatz(number: int) -> int:
    if number <= 0:
        raise ValueError("Somente inteiros positivos")
    if number == 1:
        return 1
    number = number // 2 if number % 2 == 0 else (number * 3) + 1
    return 1 + collatz(number)
