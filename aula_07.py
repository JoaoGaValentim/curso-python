"""
Higher Order Functions
Funções de primeira classe
"""

import sys


def execute(defination, *args):
    return defination(args)


def say(contents):
    content_args_value = [str(content) for content in contents]
    return " ".join(content_args_value)


def calculate_factorials(*values):
    total_fatorials_values = []
    for value in values:
        total_calculation = 1
        for i in range(value):
            total_calculation *= i + 1
        total_fatorials_values.append(total_calculation)
    return total_fatorials_values


def create_execution_pipe(*args):
    callables = []
    params = []
    callable_stack = []

    for _, arg in enumerate(args):
        is_callable = hasattr(arg, "__call__")
        if is_callable:
            callables.append(arg)
        if not is_callable:
            params.append(arg)
    for callable_function in callables:
        callable_stack.append(callable_function)

    count_stack = 0
    while count_stack < len(callable_stack):
        if count_stack > 0:
            print(callable_stack[0](callable_stack[count_stack], *params))
            callable_stack.pop(callable_stack.index(callable_stack[count_stack]))
        count_stack += 1

    count_params = 0
    if len(params) == 0:
        sys.exit(1)

    while len(params) > count_params:
        params.pop(params.index(params[count_params]))
        count_params += 1

    params.pop()


create_execution_pipe(execute, say, "Hello", 1, 2, 3)
