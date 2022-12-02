# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input("Введите число: "))
result = ""
while n > 0:
    result = str(n % 2) + result
    n //= 2
print(int(result))
