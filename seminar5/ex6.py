# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(path):
    with open(path, "r", encoding="utf-8") as file:
        input_data = list(file.readline().strip())

    # Версия без отрицательных значений
    # result = ""
    # current = input_data.pop(0)
    # counter = 1
    # for e in input_data:
    #     if e == current:
    #         counter += 1
    #     else:
    #         result += str(counter) + current
    #         current = e
    #         counter = 1
    # result += str(counter) + current
    # return result

    result = ""
    uniq_seq = ""
    repeat_seq = ""
    prev = input_data.pop(0)
    repeat_flag = False

    for el in input_data:
        if el == prev:
            if uniq_seq:
                result += str(-len(uniq_seq)) + uniq_seq
                uniq_seq = ""
            repeat_flag = True
            repeat_seq += prev
        else:
            if repeat_flag:
                repeat_flag = False
                repeat_seq += prev
                result += str(len(repeat_seq)) + repeat_seq[0]
                repeat_seq = ""
            else:
                uniq_seq += prev
        prev = el

    if input_data[-1] == input_data[-2]:
        repeat_seq += input_data[-1]
    else:
        uniq_seq += input_data[-1]
    if repeat_seq:
        result += str(len(repeat_seq)) + repeat_seq[0]
    if uniq_seq:
        result += str(-len(uniq_seq)) + uniq_seq
    with open("output6_1.txt", "w", encoding="utf-8") as file:
        file.write(result)


def decode(path):
    with open(path, "r", encoding="utf-8") as file:
        input_data = list(file.readline().strip())

    # Версия без отрицательных значений
    # result = ""
    # tmp = ""
    # for el in input_data:
    #     if el.isdigit():
    #         tmp += el
    #     else:
    #         if tmp:
    #             result += el * int(tmp)
    #         tmp = ""
    # return result

    result = ""
    tmp = ""
    for el in input_data:
        if el.isdigit() or el == "-":
            tmp += el
        else:
            if tmp and int(tmp) > 0:
                result += el * int(tmp)
            else:
                result += el
            tmp = ""
    with open("output6_2.txt", "w", encoding="utf-8") as file:
        file.write(result)


print(encode("input6_1.txt"))
print(decode("input6_2.txt"))
