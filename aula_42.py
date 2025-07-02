# count é um iterador sem fim (itertools)
from itertools import count

counter = count(10, 10)

# print(next(counter), hasattr(counter, "__iter__"))
# print(next(counter), hasattr(counter, "__next__"))

for i in counter:
    print("counter = ", i)
    if i == 100:
        break

for i in range(10, 100):
    print(i)
