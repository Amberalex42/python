# Подсчитать сумму цифр в вещественном числе.

origin = a = float(input("Введите вещественное число: "))

while a != int(a):
    a *= 10
total = 0
while a > 0:
    total += a % 10
    a //= 10
print(f"Сумма цифр числа {origin} равна {int(total)}.")
