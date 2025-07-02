"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
 H   e   l   l   o  ,     W  o  r  l  d  !
-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""

text = "Hello, World!"
print(len(text))
print(text[0:8])
print(text[-7:-1])
print(text[::-1])  # inverter
