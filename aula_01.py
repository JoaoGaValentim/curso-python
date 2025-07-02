"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

# def Print(value):
#     print(value)


# Print("Vários 1")
# Print("Vários 2")
# Print("Vários 3")
# Print("Vários 4")


def show_message(*arg, sep="", end="\n"):
    print(*arg, sep=sep, end=end)


show_message(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=".")
show_message(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, sep="x")
show_message(21, 22, 23, 24, 25, 26, 27, 28, 29, 30, sep="/")
