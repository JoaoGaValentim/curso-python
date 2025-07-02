"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""


def show_message(*arg, sep="", end="\n"):
    print(*arg, sep=sep, end=end)


def multiply_all(*args):
    try:
        total_result = 1
        for value in args:
            total_result *= value if value > 0 else 1
        return total_result
    except TypeError:
        return 0


show_message(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep="-")
show_message()
values = 1.369693936936993663, 2, 3, 4, 5, 6, 7, 8, 9, 10
total_multiply = multiply_all(*values)
show_message(f"Total: {total_multiply:.2f}")
