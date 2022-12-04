# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("Введите значение степени k: "))
d = {i: random.randint(0, 100) for i in range(k, -1, -1)}
filt_d = {k: v for k, v in d.items() if v != 0}


def get_string(d):
    result = []
    for el in d:
        if el > 1:
            if d[el] > 1:
                result.append(f"{d[el]}x^{el}")
            elif filt_d[el] == 1:
                result.append(f"x^{el}")
        elif el == 1:
            if filt_d[el] > 1:
                result.append(f"{d[el]}x")
            elif d[el] == 1:
                result.append("x")
        else:
            result.append(str(d[el]))
    return result


with open("output_4.txt", "w", encoding="utf-8") as file:
    file.write(" + ".join(get_string(filt_d)) + " = 0")
