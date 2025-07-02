# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def generator(start=0, end=10):
    step = 1 if start < end else -1
    current = start
    while current != end:
        yield current
        current += step
    yield 0


gen = generator(start=20, end=0)
start_value, end_value = 0, 1
for value in gen:
    print(start_value)
    start_value, end_value = end_value, start_value + end_value
