# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    file = open("peoples.json")
    file.close()
except FileNotFoundError as e:
    print(e.__class__.__name__)
else:
    print("Sem erros")
finally:
    print("Fim de execução")
