alien = {
    "color": "green",
    "points": 5,
}

for key, value in alien.items():
    print(key, value)


data = {
    key: value.upper() if isinstance(value, str) else value
    for key, value in alien.items()
    if key == "color"
}
print(data)

aliens = [
    ("color", "green"),
    ("color", "red"),
    ("color", "blue"),
    ("color", "orange"),
]

aliens = [{key: value} for key, value in aliens]
print(aliens)

sets_points = {i + 1 for i in range(10)}
print(sets_points)
