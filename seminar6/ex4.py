# Подсчитать сумму цифр в вещественном числе.

num_str = input("Введите число: ")
print(f"Сумма цифр числа = {sum(map(int, filter(lambda x: x != '.', num_str)))}")
