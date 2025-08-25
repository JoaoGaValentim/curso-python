import os
import random

# modos: w, r, x
# a (escreve no final)
# t (modo texto)
# + (habilita escrita e leitura)
# caminho do arquivo no mac
file_path = "/Users/joao/notas.txt"

with open(file_path, "w+") as file:
    student_points = [random.SystemRandom().uniform(0.0, 10.0) for _ in range(10)]
    file.writelines((f"{point:.2f}\n" for point in student_points))
    file.seek(0, 0)
    for data in file.readlines():
        print(data)

os.remove(file_path)
