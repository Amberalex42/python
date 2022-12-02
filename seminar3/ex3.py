# Напишите программу, которая определит позицию второго вхождения строки в списке либо
# сообщит, что её нет.

# my_list = input("Введите числа через пробел: ").split()
# f_num = input("Введите искомое число: ")


# def find_second(my_list, f_num):
#     count = 0
#     for i in range(len(my_list)):
#         if f_num in my_list[i]:
#             count += 1
#             if count == 2:
#                 return i
#             else:
#                 return -1

def find_second(my_list, f_num):
    count = 0
    res = -1
    for i in range(len(my_list)):
        if f_num == my_list[i]:
            count += 1
            if count == 2:
                res = i
                break
    return res


print(find_second(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"))
