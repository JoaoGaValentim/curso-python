# Yield from


def gen_even(n=10):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def gen_odd(n=10):
    for i in range(n + 1):
        if i % 2 == 1:
            yield i
    # yield from gen_even()


even_values_gen = gen_even()
if even_values_gen is not None:
    for value in even_values_gen:
        print(value)
