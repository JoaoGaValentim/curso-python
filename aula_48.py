# Funções recursivas e recursividadeMore actions
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
def fibonnaci(value):
    if value <= 1:
        return value
    return fibonnaci(value - 1) + fibonnaci(value - 2)


def sum_values(list_values):
    if not list_values:
        return 0
    return list_values[0] + sum_values(list_values[1:])


def get_odds(list_values=[], values=[]):
    if values is None:
        values = []

    if not list_values:
        return values

    if list_values[0] % 2 == 1:
        values.append(list_values[0])

    get_odds(list_values[1:], values)
    return values


values = [i + 1 for i in range(73)]
print(get_odds(values))
