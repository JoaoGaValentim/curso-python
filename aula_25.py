# dir, hasattr e getattr em Python
text = "Lorem"
method = "upper"

# print(*dir(text), sep=" - ")

if hasattr(text, method):
    print(getattr(text, method)())
if not hasattr(text, method):
    print("Not Found attr")
