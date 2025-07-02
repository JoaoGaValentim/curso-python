"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

Os números de ponto flutuante são representados no hardware do computador como
frações de base 2 (binárias). Por exemplo, a fração decimal 0.625 tem valor 6/10
+ 2/100 + 5/1000, e da mesma forma a fração binária 0.101 tem valor
0/2 + 0/4 + 1/8. Essas duas frações têm valores idênticos, a única diferença
real é que a primeira é escrita em notação fracionária de base 10 e a segunda
em base 2.

Infelizmente, muitas frações decimais não podem ser representadas precisamente
como frações binárias. O resultado é que, em geral, os números decimais de ponto
flutuante que você digita acabam sendo armazenados de forma apenas aproximada,
na forma de números binários de ponto flutuante.
"""

"""
import decimal 
usado em casos de extrema precisão
"""

import decimal

figure_scale_in_ym = decimal.Decimal(0.222 * 1000)
figure_scale_in_mm = decimal.Decimal(0.222)
figure_scale_in_cm = figure_scale_in_mm / 10
figure_scale_in_metters = figure_scale_in_cm / 100
figure_scale_in_km = figure_scale_in_metters / 1000
print(round(figure_scale_in_cm, 4))
print(f"{figure_scale_in_km}")
