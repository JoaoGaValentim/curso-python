# Exercício - Adiando execução de funções
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def create_defination(function, x):
    def internal_defination(y):
        return function(x, y)

    return internal_defination


add_five = create_defination(add, 5)
multiply_to_ten = create_defination(multiply, 10)

print(add_five(10))
print(multiply_to_ten(10))
