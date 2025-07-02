# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

# try:
#     sys.path.append("Users")
# except ModuleNotFoundError as e:
#     print(e)
# import aula_35_m
from aula_35_m import first_name

print(sys.path)

print("Módulo é", __name__)
print(first_name)

for path in sys.path:
    print(path.replace("/", " => "))
