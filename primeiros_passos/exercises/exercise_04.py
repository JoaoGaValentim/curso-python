name = input("Informe seu nome: ")

if name:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    print(f"Seu nome {'contém' if ' ' in name else 'não contém'} espaços em branco")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A ultima letra do seu nome é {name[len(name) - 1]}")
if not name:
    print("Desculpe, você deixou campos vazios")
