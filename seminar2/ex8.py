# Реализовать алгоритм перемешивания списка.
import random

a = [1, 2, 3, 4, 5, 6]
result = []
while len(a) > 0:
    result.append(a.pop(random.randint(0, len(a) - 1)))
print(result)
