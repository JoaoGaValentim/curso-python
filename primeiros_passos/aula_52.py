# Desempacotamento em chamadas
# de métodos e funções


classrooms = [
    ["João", "Clara"],
    ["Lucas", "Ana"],
    ["José", "Pedro", "Maria", (7, 8, 10)],
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeral_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeral_tuple = 1, 2, 3

numeral_zero, numeral_one, *_ = numeral_list
print(numeral_zero, numeral_one)

# for number in numeral:
#     print(number, end=" ")

print(*numeral_list)
print(*numeral_tuple)
print(*alphabet)
print(*classrooms)
