# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def calculate(value):
    def multiply(value_factor):
        return value * value_factor

    return multiply


for i in [2, 3, 4]:
    execute_operation = calculate(2)
    print(execute_operation(i))
