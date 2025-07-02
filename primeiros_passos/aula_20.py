# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3
#  J o ã o
# -4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)
# name = "João"
# print("J" in name)
# print("oã" in name)
# print("o" in name)
# print("ã" in name)
# print("J" not in name)
# print("o" not in name)
# print("a" not in name)
# print(name[-4])  # J
# print(name[-3])  # o
# print(name[-2])  # ã
# print(name[-1])  # o

name = input("Digite seu nome => ")
search = input("Oque quer encontrar? ")

if search in name:
    print(f"Argumento(s): {search} está em nome")
