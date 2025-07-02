"""
For + Range
range -> range(start, stop, step)
"""

name = "Joao Gabriel Valentim Theodoro"
text = ""
for i in range(len(name)):
    text += name[i].upper() + str(i)
print(text, end="")
