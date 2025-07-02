"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# try:
#     file = open("dados.txt", "r")
# except FileNotFoundError as e:
#     print(e)

try:
    number_str = input("Digite Um número: ")
    double = float(number_str) * 2
    print(f"O Dobro de {number_str} é {double}.")
except ValueError:
    print("Não é um número!")
