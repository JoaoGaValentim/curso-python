"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import random
import re


def cpf_sanitizer(fun):
    def wrapper(*args):
        cpf = fun(*args)
        cpf = re.sub(r"[^0-9]", "", cpf)
        return cpf

    return wrapper


@cpf_sanitizer
def get_sanitized_cpf(cpf):
    return cpf


def get_first_digit(cpf):
    cpf_counter_value_to_first_digits = 10
    cpf_first_digit_value = 0
    for cpf_digit in cpf:
        cpf_first_digit_value += int(cpf_digit) * cpf_counter_value_to_first_digits
        cpf_counter_value_to_first_digits -= 1
    cpf_first_digit_value = cpf_first_digit_value * 10
    cpf_first_digit_value = (
        cpf_first_digit_value % 11 if cpf_first_digit_value % 11 <= 9 else 0
    )
    return cpf_first_digit_value


def get_last_digit(cpf):
    cpf_first_digits = cpf[:9] + str(get_first_digit(cpf))
    cpf_counter_value_to_last_digits = 11
    cpf_last_digit_value = 0
    for cpf_digit in cpf_first_digits:
        cpf_last_digit_value += int(cpf_digit) * cpf_counter_value_to_last_digits
        cpf_counter_value_to_last_digits -= 1

    cpf_last_digit_value = cpf_last_digit_value * 10
    cpf_last_digit_value = (
        cpf_last_digit_value % 11 if cpf_last_digit_value % 11 <= 9 else 0
    )
    return cpf_last_digit_value


def generate_cpf():
    cpf = ""
    for _ in range(0, 9):
        cpf += str(random.randint(0, 9))
    cpf = get_sanitized_cpf(cpf)[:9]
    first_digit = get_first_digit(cpf)
    last_digit = get_last_digit(cpf)
    return f"{cpf}{first_digit}{last_digit}"


def get_random_cpf_with_mask():
    pattern = r"^(\d{3})(\d{3})(\d{3})(\d{2})$"
    replacement = r"\1.\2.\3-\4"
    cpf = generate_cpf()
    return re.sub(pattern, replacement, cpf)


def validate_cpf(cpf: str) -> bool:
    cpf_clean = get_sanitized_cpf(cpf)

    if len(cpf_clean) != 11 or cpf_clean == cpf_clean[0] * 11:
        return False

    try:
        firs_digit = get_first_digit(cpf_clean[:9])
        last_digit = get_last_digit(cpf_clean[:9])
    except ValueError:
        return False

    return cpf_clean.endswith(f"{firs_digit}{last_digit}")


def main(range_cpf: int = 100):
    cpfs: list[str] = []
    print("=" * 22)
    for i in range(range_cpf):
        cpf = get_random_cpf_with_mask()
        cpfs.append(cpf)
        print(f"CPF {i + 1}: {cpf}")
    print("=" * 22)

    try:
        with open("primeiros_passos/exercises/cpfs.txt", "a") as file:
            file.writelines(["\n".join(cpfs)])
    except IOError as e:
        print(e)

    for cpf in cpfs:
        print(cpf, "Válido" if validate_cpf(cpf) else "Inválido")


if __name__ == "__main__":
    main()
