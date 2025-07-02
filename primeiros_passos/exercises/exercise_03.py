

first_number = input("Informe um valor: ")
last_number = input("Informe outro valor: ")

is_digit = first_number.isdigit() and last_number.isdigit()

if is_digit:
    first_number_casting = int(first_number)
    last_number_casting = int(last_number)
    state_existence = (
        f"1º valor {first_number=} é maior/ou igaul que {last_number=}"
        if first_number >= last_number
        else f"2º valor {last_number=} é maior/ou igual que {first_number=}"
    )
    print(state_existence)
