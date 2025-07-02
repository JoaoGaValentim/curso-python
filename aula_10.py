# Manipulando chaves e valores em dicionários
import random

user = {}

user_name_key = "name"
user[user_name_key] = "João Gabriel Valentim Theodoro"

print(user)
user[user_name_key] = "João Gabriel"
# print(user["age"])  # KeyError: 'age'
del user[user_name_key]
if user.get("name") is not None:
    print(user[user_name_key])
if user.get("name") is None:
    user[user_name_key] = "João"

print(user)

keys = [random.randint(1, 1000) for _ in range(11)]
rand_dict = {}

for key in keys:
    rand_dict[key] = key


print(rand_dict)
