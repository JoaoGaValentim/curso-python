"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

from string import Template

name = "João"
price = 1000.9034325759
content = "%s o preço é %f"
print(content % (name, price))

template = Template("$name o preço é $price")
print(template.substitute(name=name, price=price))

print("O hex de um número %d é %x" % (15, 255))
print(f"O hex {15:x} é {15}")
