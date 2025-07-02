"""while/else"""

string = "Joao Theodoro"

i = 0

while i < len(string):
    letter = string[i]
    print(letter)

    if letter == " ":
        break

    i += 1
else:
    print("Fim.")
