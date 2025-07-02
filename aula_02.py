"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual -> set_postion(x=10, y=20)
Argumento não nomeado recebe apenas o argumento (valor) -> sum(1, 2)
"""


def get_fats(*numbers):
    try:
        fat = 1
        fats_results = []
        for number in numbers:
            fat = 1
            for i in range(number):
                fat *= i + 1
            fats_results.append(fat)
        return fats_results
    except TypeError as e:
        return e.args[0]


def get_json(**kwargs):
    try:
        latitude = float(kwargs.get("latitude", 0.0))
        longitude = float(kwargs.get("longitude", 0.0))
        country = kwargs.get("country", None)

        return {"latitude": latitude, "longitude": longitude, "country": country}
    except ValueError as e:
        return e.args[0]


print(get_fats(4, 5))
print(get_json(latitude=-24554, longitude=-222.3, country="US"))
