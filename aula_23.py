# isinstace - para saber se objeto é de determinado tipo
import random


alien = {}
colors = ["green", "red", "blue"]
speeds = ["slow", "medium", "fast"]

alien["color"] = random.choice(colors)
alien["x_postion"] = 0
alien["y_postion"] = random.randint(0, 25)
alien["speed"] = random.choice(speeds)


aliens = [{key: value for key, value in alien.items()} for _ in range(10)]

for _, alien_item in enumerate(aliens):
    print(
        {
            key: (
                value.upper()
                if isinstance(value, str)
                else value // 2
                if isinstance(value, (float, int))
                else value
            )
            for key, value in alien_item.items()
        }
    )


def get_instance(*args):
    for arg in args:
        if isinstance(arg, set):
            arg.add(1)
            print(arg)
        if isinstance(arg, str):
            print(arg.upper())
        if isinstance(arg, (int, float)):
            print(arg * 2)


get_instance("update", {3}, 2)
