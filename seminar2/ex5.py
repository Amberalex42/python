# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = int(input("Введите число: "))
result = []
mult = 1
for i in range(1, n + 1):
    mult *= i
    result.append(mult)
print(f"Для N = {n} результат {result}")