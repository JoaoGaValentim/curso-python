print("*" * 20)
print("Calculadora".upper().center(20))
print("*" * 20)

is_running = True

while is_running:
    print("*" * 20)
    print("[+] para soma".upper().center(20))
    print("[-] para subtração".upper().center(20))
    print("[*] para multiplicação".upper().center(20))
    print("[/] para divisão".upper().center(20))
    print("[s ou q] para sair")
    print("*" * 20)
    cmd = input("Entrada de comando >> ").lower()

    if cmd == "q" or cmd == "s":
        print("*" * 20)
        print("Até Logo :)".upper().center(20))
        print("*" * 20)
        break

    number_input_x = input("Valor inicial: ")
    number_input_y = input("Valor secundario: ")
    is_number = number_input_x.isnumeric() and number_input_y.isnumeric()

    if is_number is True:
        number_x = float(number_input_x)
        number_y = float(number_input_y)
        if cmd == "+":
            print("*" * 20)
            print("Soma".upper().center(20))
            print("*" * 20)
            print(f"{number_x} + {number_y} = {number_x + number_y}")
        if cmd == "-":
            print("*" * 20)
            print("Subtração".upper().center(20))
            print("*" * 20)
            print(f"{number_x} - {number_y} = {number_x - number_y}")
        if cmd == "*":
            print("*" * 20)
            print("Multiplicação".upper().center(20))
            print("*" * 20)
            print(f"{number_x} x {number_y} = {number_x * number_y}")
        if cmd == "/":
            print("*" * 20)
            print("Divisão".upper().center(20))
            print("*" * 20)
            print(f"{number_x} / {number_y} = {number_x / number_y}")
    if is_number is False:
        print("*" * 20)
        print("Você deve informar somente números!".upper().center(20))
        print("*" * 20)
