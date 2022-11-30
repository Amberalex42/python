# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

n = int(input("Введите число: "))
positions = [1, 3, 6]
result = [i for i in range(-n, n + 1)]
print(result)
total = 1
for el in positions:
    if el < len(result):
        total *= result[el]
print(total)