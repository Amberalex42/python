# Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

a = int(input("Введите число: "))
condition = a % 5 == 0 and (a % 10 == 0 or a % 15 == 0) and a % 30
print("Число кратно 5 и 10 или 15, но не 30" if condition else "Число не выполняет условие")
