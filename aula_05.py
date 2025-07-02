"""
Retorno de valores das funções (return)
"""

# def get_date():
#     print(7**8)


def calculate_fat(number=1):
    fat_result = 1
    if number <= 0:
        return 1
    for i in range(number):
        fat_result *= i + 1
    return number, fat_result


fat_total_calculation = calculate_fat(5)
# any_value = int("1")
# print(any_value)
# print(fat(5))
# print(fat(6))
# print(fat(7))
# print(get_date())
print(fat_total_calculation)
