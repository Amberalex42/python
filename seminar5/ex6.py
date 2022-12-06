# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def decode(path):
    with open(path, "r", encoding="utf-8") as file:
        input_data = list(file.readline().strip())
    result = input_data[0]
    for i in range(len(input_data) - 1):
        if


print(decode("input6_1.txt"))
