# \r\n -> quebra no Windows -> CRLF
# \n -> Linux e Mac -> LF
print("|", 12, 34, "|")  # argumentos nao nomeados
print("|", 56, 78, "|")
print("|", 10, 11, "|")
print("|", 12, 34, "|")
print("|", 56, 78, "|")
print("|", 10, 11, "|")
print("x", "x", sep="__", end="\t")  # argumentos nomeados
print("x", "x", sep="__", end="\t\n")
print(14, 4, 2001, sep=" / ")
print("https:/", "joao.com", sep="/")
