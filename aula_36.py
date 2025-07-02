import importlib
import aula_36_m


for value in aula_36_m.pi_multiply_gen:
    importlib.reload(aula_36_m)
    print(value)
