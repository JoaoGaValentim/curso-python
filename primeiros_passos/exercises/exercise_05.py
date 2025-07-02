try:
    number_input = input("Informe um número inteiro: ")
    number = int(number_input)

    if number % 2 == 0:
        print(f"{number=} é par")
    if number % 2 == 1:
        print(f"{number=} é impar")

except ValueError:
    print("Informe um número inteiro")
