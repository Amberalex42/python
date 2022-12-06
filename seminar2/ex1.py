# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N
# членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите число: "))
result = []
for i in range(n):
    result.append(str((-1)**i * 3**i))
print(f"Для N = {n}: {', '.join(result)}")