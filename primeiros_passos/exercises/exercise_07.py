name_input = input("Qual o seu nome? ")
name_size = len(name_input)

is_small = name_size <= 4
is_medium = name_size >= 5 and name_size <= 6
is_big = name_size > 6

if is_small:
    print("Seu nome é curto")
if is_medium:
    print("Seu nome é normal")
if is_big:
    print("Seu nome é muito grande")
