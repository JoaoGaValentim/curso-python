"""
enumerate - enumera iteráveis (índices)
"""

animals_names_list = ["Bobó", "Scooby", "Luna"]
# animals_names_list_enum = list(enumerate(animals_names_list, start=1))
# print(animals_names_list, next(animals_names_list_enum))
# print(animals_names_list, next(animals_names_list_enum))
# print(animals_names_list, next(animals_names_list_enum))

# for item in enumerate(animals_names_list, start=1):
#     print("FOR INTERNO")
#     for animal_name in item:
#         print(f"\t{animal_name}")
for index, animal_name in enumerate(animals_names_list, start=1):
    print(f"{index} - {animal_name}")
