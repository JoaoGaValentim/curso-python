"""
split e join com list e str
split - divide uma string (list)
join - une uma string


print(phrase[i].strip()) Remove space left and right
print(phrase[i].lstrip()) Remove space left
print(phrase[i].rstrip()) Remove space right

"""

message_of_day = "Seja um qubit melhor hoje!"
message_of_day_splited_list = message_of_day.split()
print(message_of_day_splited_list)

fake_phrase = "    Olha esse grupo de palavras, legal demais    "

fake_phrase_list = fake_phrase.split(",")
fake_phrase_fixed_list = []
for i, phrase in enumerate(fake_phrase_list):
    fake_phrase_fixed_list.append(fake_phrase_list[i].strip())
print(fake_phrase_fixed_list)

fake_phrases_union = ",".join(fake_phrase_fixed_list)
print(fake_phrases_union)
