# Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

with open("input_5_1.txt", "r", encoding="utf-8") as file:
    line1 = file.readline().strip()
with open("input_5_2.txt", "r", encoding="utf-8") as file2:
    line2 = file2.readline().strip()


def line_to_dict(line):
    result = dict()
    lst = line.strip(" = 0").split(" + ")
    for el in lst:
        if "x" in el:
            tmp = el.split('x')
            result[int(tmp[1].strip("^")) if tmp[1] else 1] = int(tmp[0]) if tmp[0] else 1
        else:
            result[0] = int(el)
    return result


def sum_dict(d1, d2):
    for el in d2:
        d1[el] = d1.get(el, 0) + d2[el]
    return dict(sorted(d1.items(), reverse=True))


def dict_to_string(d):
    result = []
    for el in d:
        if el > 1:
            if d[el] > 1:
                result.append(f"{d[el]}x^{el}")
            elif d[el] == 1:
                result.append(f"x^{el}")
        elif el == 1:
            if d[el] > 1:
                result.append(f"{d[el]}x")
            elif d[el] == 1:
                result.append("x")
        else:
            result.append(str(d[el]))
    return " + ".join(result) + " = 0"


d1 = line_to_dict(line1)
d2 = line_to_dict(line2)
sum_d = sum_dict(d1, d2)
with open("output5.txt", "w", encoding="utf-8") as file3:
    file3.write(dict_to_string(sum_d))
