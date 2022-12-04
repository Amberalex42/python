# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

# k = int(input("Введите значение степени k: "))
# d = {i: random.randint(0, 1) for i in range(k, -1, -1)}
koef = [0, 1, 0, 1, 1]
d = {i: koef[i] for i in range(4, -1, -1)}
filt_d = {k: v for k, v in d.items() if v != 0}
print(filt_d)
str_poly = ""
if not len(filt_d):
    str_poly = "0 = 0"
elif len(filt_d) == 1 and 0 in filt_d:
    str_poly = "Произошла ошибка при определении коэффициентов."
else:
    koef_list = []
    for el in d:
        if el != 1:
            pass
        else:
            pass
    print([f"{v}x^{k}" if v != 1 else f"x^{k}" for k, v in filt_d.items()])
#     for el in filt_d:
#         if el > 1:
#             str_poly += f"{filt_d[el] if filt_d[el] != 1 else ''}x^{el} "
#         elif el == 1:
#             str_poly += f"+ {filt_d[el] if filt_d[el] > 1 else ''}x "
#         else:
#             str_poly += f"+ {filt_d[el]} "
#     str_poly += "= 0"
# print(str_poly)
# with open("output_4.txt", "w", encoding="utf-8") as file:
#     file.write(str_poly)
