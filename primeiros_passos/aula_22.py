"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

value = "ABC"
print(f"{value: >20}")
print(f"{value: <20}")
print(f"{value:^10}")
print(f"{1000.234124234137:0=+10,.2f}")
print(f"O hexadecimal de 100 é {1500:08X}")
print(f"{value!r}")
