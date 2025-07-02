"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

sum = 0

is_running = True

while is_running:
    number_input = input("Informe um valor: ")
    is_numberic_digit = number_input.isdigit()
    if is_numberic_digit:
        number = int(number_input)
        sum += 1
    if not is_numberic_digit:
        print("Não posso continuar, informe somente números inteiros.")
        is_running = False

print(f"Soma = {sum}")
