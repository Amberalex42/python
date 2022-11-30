# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
result = []
for el in lst:
    if not isinstance(el, int):
        result.append(el - int(el))
max_el = min_el = result[0]
for el in result:
    if el > max_el:
        max_el = el
    elif el < min_el:
        min_el = el
print(max_el - min_el)
