# Exercícios com funções


# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiply_all(*args: int) -> float:
    try:
        total_result = 1
        for value in args:
            total_result *= value if value > 0 else 1
        return total_result
    except TypeError as e:
        print(e)
        return 0


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def is_even_or_odd(*args):
    try:
        count_str_index = 0
        for index, value in enumerate(args, start=1):
            type_is_str = type(value) is str
            if index >= 1 and index <= len(args) and type_is_str:
                count_str_index += 1
                if count_str_index >= 1:
                    break
            if value % 2 == 0:
                print(f"{value} é par.")
                if value % 2 == 1:
                    print(f"{value} é impar.")
    except TypeError as e:
        print(e.args[0])


is_even_or_odd(10, 20, 30, 35, 2, 1)
