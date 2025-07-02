"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

loop = True

while loop:
    value = input("Entre com um valor: ")
    if value == "A" or value == "a":
        loop = False
