# if / elif      / else
# se / se não se / se não


input_cmd = input("Quer 'Entrar' ou 'Sair'? ")

if input_cmd.lower() == "entrar":
    print("Logado")
elif input_cmd.lower() == "sair":
    print("deslogado")
else:
    print("Comando não encontrado")

print("=== comandos completados ===")
