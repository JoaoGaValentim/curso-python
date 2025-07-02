# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

values = [1]  # [] Falsy
letters = {1, 3}
colors = set({1})
coords = (2,)
text = " "
age = 2  # 0 Falsy
heigh = 0.1  # 0.0 Falsy
is_none = not None  # If is None then is Falsy
is_real = False
interval = range(0)


def test_truthy_and_falsy(*args):
    tests = []
    for arg in args:
        tests.append(f"{arg=} is Falsy" if not arg else f"{arg=} is Truthy")
    return tests


result_test = test_truthy_and_falsy(
    values,
    letters,
    colors,
    coords,
    text,
    age,
    heigh,
    is_none,
    is_real,
    interval,
)

for result in result_test:
    print(result)
