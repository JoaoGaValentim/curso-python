phrase = (
    "João odeia psicologos, pois,"
    "são papeis higiênicos, usa-se para um problema, mas sempre usa para"
    "limpar outro"
)

# sum
most_common_letter = None
most_common_count = 0
i = 0
# filter chars
while i < len(phrase):
    letter = phrase[i]

    if letter == " ":
        i += 1
        continue

    count_occurrences = phrase.count(letter)

    if count_occurrences > most_common_count:
        most_common_letter = letter
        most_common_count = count_occurrences

    i += 1


print(
    f'A letra que aparteceu mais vezes foi "{most_common_letter}" '
    f"aparecendo {most_common_count}x"
)
