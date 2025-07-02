"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

sum = 0
count = 0

while sum <= 10:
    number_input = input("Informe um valor: ")
    is_numberic_digit = number_input.isdigit()
    if is_numberic_digit:
        number = int(number_input)
        count += number
    if not is_numberic_digit:
        print("Informe somente números inteiros.")
        continue
    sum += 1

print(f"Soma = {count}")
