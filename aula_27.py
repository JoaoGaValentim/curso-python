# Generator expression, Iterables e Iterators em Python

import sys

numbers_generator = (number for number in range(10000000))
print(sys.getsizeof(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator) - 1)
print(next(numbers_generator) - 1)
print(next(numbers_generator) - 1)
print(next(numbers_generator))
