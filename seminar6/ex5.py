# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

lst = input("Введите список строк через пробел: ")
num = input("Введите число: ")
print("Присутствует" if len(tuple(filter(lambda x: num in x, lst.split()))) else "Отсутствует")
