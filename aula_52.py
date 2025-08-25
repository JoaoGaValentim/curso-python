import json
from typing import Any

# people = {
#     "first_name": "João Gabriel Valentim",
#     "last_name": "Theodoro",
#     "age": 24,
#     "languages": ["Java", "Python", "C++"],
#     "points": None,
#     "is_developer": True,
# }

with open("peoples.json", "r") as file:
    peoples: dict[Any, Any] = json.load(file)
    print(peoples, type(peoples))
    name, last_name, age, *_ = peoples.values()
    print(age)
