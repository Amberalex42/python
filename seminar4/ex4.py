# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("Введите значение степени k: "))
d = {i: random.randint(0, 100) for i in range(k, -1, -1)}
str_poly = ""
for el in d:
    if el != 0:
        str_poly += f"{d[el]}x^{el} + "
    else:
        str_poly += f"{d[el]} = 0"
with open("output_4.txt", "w", encoding="utf-8") as file:
    file.write(str_poly)
