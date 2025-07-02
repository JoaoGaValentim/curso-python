"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

is_legal = False
name = None

# if is_legal:
#     name = "João"
#     print(is_legal)


print(name if name is not None else None)
print(name, name is not None)
print(name, name is None)
