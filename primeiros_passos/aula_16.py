"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

from string import Template

greater_than = 12 < 11
greater_or_eq_than = 12 >= 12
equals = 12 == "12"
different_from = 11 != 12

s_template = Template("$greater_than, $greater_or_eq_than, $equals & $different_from")

print(
    s_template.substitute(
        greater_than=greater_than,
        greater_or_eq_than=greater_or_eq_than,
        equals=equals,
        different_from=different_from,
    )
)
