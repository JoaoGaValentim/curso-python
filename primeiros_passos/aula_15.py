# if / elif      / else
# se / se não se / se não
age_input = input("informe sua idade >> ")

age = int(age_input)

is_legal_age = age >= 18

gender = input("Entre com seu gênero (M, F) >> ").lower()

if is_legal_age and gender == "m":
    print("É maior de idade e é homem!")
if is_legal_age and gender == "f":
    print("É maior de idade e é mulher!")
if not is_legal_age and gender == "m":
    print("Não é maior de idade e é homem!")
if not is_legal_age and gender == "f":
    print("Não é maior de idade e é mulher!")

print("=== comandos completados ===")
