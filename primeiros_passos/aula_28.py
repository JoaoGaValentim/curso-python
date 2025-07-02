"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool

 J   o   a   o
-4  -3  -2  -1
"""

string = "João"
other_string = f"{string[-4::3]}X{string[-3::3]}"

print(other_string)
print(string.zfill(10))
