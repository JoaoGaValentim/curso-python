"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

columns = 10
rows = 10

rows_i = 1
while rows_i <= rows:
    columns_i = 1
    while columns_i <= columns:
        print(f"{rows_i=}, {columns_i=}")
        columns_i += 1
    rows_i += 1
