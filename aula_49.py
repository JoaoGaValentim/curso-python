# Funções recursivas e recursividadeMore actions
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
import sys

sys.setrecursionlimit(1000)


def is_prime(number=0, count=2):
    if number <= 1:
        return number
    if count * count > number:
        return True
    if number % count == 0:
        return False
    return is_prime(number, count + 1)


count = 0
for i in range(137):
    if is_prime(i + 1):
        count += 1
        print(count, i + 1)
